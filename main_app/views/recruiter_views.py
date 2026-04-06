from django.views.generic import CreateView,DetailView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Prefetch
from main_app.forms import SignUpFormRecruiter
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
        group = Group.objects.get(name="recruiter")
        user.groups.add(group) # adding user to recruiter group for permission management
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

class ProcessApplication(LoginRequiredMixin,RoleCheckMixin,DetailView):
    role = "REC"
    model = Application 
    template_name = ""
    context_object_name = "application"
    login_url = "/login/"

    def get_object(self):
        applicant_profiles = Prefetch(
            'applicant__applicant_profile',
            queryset=ApplicantProfile.objects.prefetch_related('skills')
        )
        
        return Application.objects.filter(
            id = self.kwargs.get('application_id')
        ).select_related('applicant').prefetch_related(applicant_profiles)