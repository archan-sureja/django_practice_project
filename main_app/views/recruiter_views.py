from django.views.generic import CreateView,View
from django.shortcuts import redirect , render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Prefetch
from main_app.forms import EditJobForm, SignUpFormRecruiter, ChangeStatus , CreateJobForm
from main_app.models import Application, RecruiterProfile, Job, User, ApplicantProfile
from main_app.views.common_views import ListView
from main_app.views.common_views import RoleCheckMixin

class SignupRecruiter(CreateView):
    form_class = SignUpFormRecruiter
    template_name = "auth/sign_up.html"
    success_url = "/login/"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = "REC"
        # group = Group.objects.get(name="recruiter")
        # user.groups.add(group) # adding user to recruiter group for permission management
        user.save()
        #pylint: disable=E1101
        RecruiterProfile.objects.filter(user=user).update(
                company=form.cleaned_data.get("company"),
                experience=form.cleaned_data.get("experience")
        ) 
        response = super().form_valid(form)
        messages.success(self.request,"Signed up successfully , Now you can login")
        return response
    
class RecruiterDashboard(LoginRequiredMixin,RoleCheckMixin, ListView):
    role = "REC"
    model = Job 
    template_name = "recruiter/dashboard.html"
    context_object_name = "jobs"
    ordering = ["-posted_at"]
    login_url = "/login/"

    def get_queryset(self):
        # applications_with_applicants = Prefetch("applications", queryset=Application.objects.select_related("applicant"))#pylint: disable=E1101
        return Job.objects.filter(posted_by=self.request.user)
    

class JobWiseApplications(LoginRequiredMixin,RoleCheckMixin,ListView):
    role = "REC"
    model = Application
    template_name = "recruiter/job_wise_applications.html"
    context_object_name = "applications"
    login_url = "/login/"

    def get_queryset(self):
        # Prefetch applicant profile with skills to avoid N+1 queries
        applicant_profiles = Prefetch(
            'applicant__applicant_profile',
            queryset=ApplicantProfile.objects.prefetch_related('skills')
        )
        
        return Application.objects.filter(
            job_id=self.kwargs.get("job_id")
        ).select_related('applicant').prefetch_related(applicant_profiles)

class ProcessApplication(LoginRequiredMixin,RoleCheckMixin,View):
    role = "REC"
    login_url = "/login/"

    def get(self,request,*args,**kwargs):
        applicant_profiles = Prefetch(
            'applicant__applicant_profile',
            queryset=ApplicantProfile.objects.prefetch_related('skills')
        )
        
        application =  Application.objects.filter(
            id = self.kwargs.get('application_id')
        ).select_related('applicant').prefetch_related(applicant_profiles)[0]
        form = ChangeStatus(initial={"status":application.status})
        return render(request,"recruiter/process_application.html",{"application":application,"form":form})
    
    def post(self,request,*args,**kwargs):
        form = ChangeStatus(request.POST)
        if form.is_valid():
            application = Application.objects.get(id=self.kwargs.get('application_id')) #pylint: disable=E1101
            application.status = form.cleaned_data.get("status")
            application.save()
            messages.success(request,"Application status updated successfully")
            return redirect("job_wise_applications",job_id=application.job.id)
        else:
            messages.error(request,"Invalid data")
            return redirect("process_application",application_id=self.kwargs.get('application_id'))

class CreateJob(LoginRequiredMixin,RoleCheckMixin,CreateView):
    role = "REC"
    model = Job
    form_class = CreateJobForm
    template_name = "recruiter/create_job.html"
    login_url = "/login/"

    def form_valid(self, form):
        job = form.save(commit=False)
        job.posted_by = self.request.user
        job.save()
        messages.success(self.request,"Job created successfully")
        return redirect("recruiter_dashboard")

class EditJob(LoginRequiredMixin,RoleCheckMixin,View):
    role = "REC"
    login_url = "/login/"

    def get(self,request,*args,**kwargs):
        job = Job.objects.get(id=self.kwargs.get("job_id"),posted_by=self.request.user) #pylint: disable=E1101
        form = EditJobForm(instance=job)
        return render(request,"recruiter/edit_job.html",{"form":form,"job":job})
    
    def post(self,request,*args,**kwargs):
        job = Job.objects.get(id=self.kwargs.get("job_id"),posted_by=self.request.user) #pylint: disable=E1101
        form = EditJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            messages.success(request,"Job updated successfully")
            return redirect("recruiter_dashboard")
        else:
            messages.error(request,"Invalid data")
            return render(request,"recruiter/edit_job.html",{"form":form,"job":job})