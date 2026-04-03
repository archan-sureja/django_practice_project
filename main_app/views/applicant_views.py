from django.views import View 
from django.views.generic import DetailView, ListView,CreateView , UpdateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
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

class ApplyJobView(LoginRequiredMixin,RoleCheckMixin,CreateView):
    model = Application 
    role = "APP"
    login_url = "/login/"
    # fields = ["cover_letter"]
    template_name = "applicant/apply_job.html"
    success_url = "/applicant/dashboard/applications/"
    form_class = ApplicationForm
    def form_valid(self, form):
        application = form.save(commit=False)
        application.applicant = self.request.user
        application.job_id = self.kwargs.get("job_id")
        application.save()
        messages.success(self.request,"Applied for job successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = Job.objects.select_related("posted_by","company").get(pk=self.kwargs.get("job_id")) #pylint: disable=E1101
        context["application"] = Application.objects.filter(applicant=self.request.user,job_id=self.kwargs.get("job_id")).first() #pylint: disable=E1101
        return context

class UpdateApplicationView(LoginRequiredMixin,RoleCheckMixin,UpdateView):
    model = Application 
    role = "APP"
    login_url = "/login/"
    # fields = ["cover_letter"]
    template_name = "applicant/apply_job.html"
    success_url = "/applicant/dashboard/applications/"
    form_class = ApplicationForm

    def get_object(self, queryset = ...):
        return Application.objects.get(applicant=self.request.user,job_id=self.kwargs.get("job_id")) #pylint: disable=E1101

    def form_valid(self, form):
        application = form.save(commit=False)
        application.applicant = self.request.user
        application.job_id = self.kwargs.get("job_id")
        application.save()
        messages.success(self.request,"Application updated successfully")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = Job.objects.select_related("posted_by","company").get(pk=self.kwargs.get("job_id")) #pylint: disable=E1101
        context["application"] = Application.objects.filter(applicant=self.request.user,job_id=self.kwargs.get("job_id")).first() #pylint: disable=E1101
        return context