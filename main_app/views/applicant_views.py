from django.views import View 
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView,CreateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.http import HttpResponseForbidden
from crispy_forms.layout import Submit
from main_app.forms import SignUpFormApplicant , ApplicationForm
from main_app.models import ApplicantProfile, Application, Job 
from main_app.views.common_views import RoleCheckMixin

class SignupApplicant(CreateView):
    form_class = SignUpFormApplicant
    template_name = "auth/sign_up.html"
    success_url = "/login/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = "APP"
        group = Group.objects.get(name="applicant")
        user.groups.add(group) # adding user to applicant group for permission management
        user.save()
        #pylint: disable=E1101
        ApplicantProfile.objects.filter(user=user).update(
                resume=form.cleaned_data.get("resume")
        ) 
        response = super().form_valid(form)
        messages.success(self.request,"Signed up successfully , Now you can login")
        return response

class ApplicantDashboard(LoginRequiredMixin,RoleCheckMixin, ListView):
    model = Job
    template_name = "applicant/dashboard.html"
    context_object_name = "jobs"
    role = "APP"
    login_url = "/login/"

    def get_queryset(self):
        return Job.objects.filter(deadline__gte=timezone.localdate(),is_active=True) #pylint: disable=E1101

class ApplicantionListView(LoginRequiredMixin,RoleCheckMixin,ListView):
    model = Application
    template_name = "applicant/application_list.html"
    context_object_name = "applications"
    role = "APP"
    login_url = "/login/"

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related("job") #pylint: disable=E1101

class ApplicantJobDetailView(LoginRequiredMixin,RoleCheckMixin,DetailView):
    model = Job
    template_name = "applicant/job_detail.html"
    context_object_name = "job"
    role = "APP"
    login_url = "/login/"

    def get_object(self, queryset = ...):
        return Job.objects.select_related("posted_by","company").get(pk=self.kwargs.get("job_id")) #pylint: disable=E1101


class JobApplicationView(LoginRequiredMixin,RoleCheckMixin,View):
    role = "APP"
    login_url = "/login/"

    def get(self, request, *args, **kwargs): 
        if self.kwargs.get("action") == "create":
            job = Job.objects.get(pk=self.kwargs.get("job_id")) #pylint: disable=E1101
            existing_application = Application.objects.filter( #pylint: disable=E1101
            job=job,
            applicant=request.user  
            ).first()
            if existing_application:
                messages.success(request,"You have already applied for this job")
                return redirect("applications")
            else:
                form = ApplicationForm()
                form.helper.add_input(Submit('submit','Apply for Job',css_class="btn btn-primary"))
        elif self.kwargs.get("action") == "update":
            existing_application = get_object_or_404(
                Application,
                id=self.kwargs.get("application_id"),
                applicant=request.user) 
            form = ApplicationForm(instance=existing_application)
            form.helper.add_input(Submit('submit','Update Application',css_class="btn btn-primary"))

        elif self.kwargs.get("action") == "withdraw":
            existing_application = get_object_or_404(
                Application,
                id=self.kwargs.get("application_id"),
                applicant=request.user) 
            existing_application.delete()
            messages.success(request,"Application withdrawn successfully")
            return redirect("applications")
        else:
            return HttpResponseForbidden("Invalid action")
        context = {
            "form": form,
            "job": job,
            "application": existing_application if self.kwargs.get("action") == "update" else None
        }
        return render(request,"applicant/apply_job.html",context)

    def post(self, request, *args, **kwargs):
        job = Job.objects.get(pk=self.kwargs.get("job_id")) #pylint: disable=E1101
        application = None
        if self.kwargs.get("action") == "update":
            application = get_object_or_404(
                Application,
                id=self.kwargs.get("application_id"),
                applicant=request.user)
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
          if application:
              application.cover_letter = form.cleaned_data.get("cover_letter")
              application.save()
              messages.success(request,"Application updated successfully")
              return redirect("applicant_dashboard")
          else:
              Application.objects.create( #pylint: disable=E1101
                  job=job,
                  applicant=request.user,
                  cover_letter=form.cleaned_data.get("cover_letter")
              )
              messages.success(request,"Applied for job successfully")
          return redirect("applications")
        return render(request,"applicant/apply_job.html",{"form":form,"job":job})