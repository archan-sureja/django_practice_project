from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib import messages
from django.db.models import Prefetch
from main_app.forms import SignUpFormRecruiter
from main_app.models import Application, RecruiterProfile,Job
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
    role_check_fail_url = "login"
    model = Job 
    template_name = "recruiter/dashboard.html"
    context_object_name = "jobs"
    paginate_by = 10
    ordering = ["-posted_at"]
    login_url = "/login/"

    def get_queryset(self):
        applications_with_applicants = Prefetch("applications", queryset=Application.objects.select_related("applicant"))#pylint: disable=E1101
        return Job.objects.filter(posted_by=self.request.user).prefetch_related(applications_with_applicants) #pylint: disable=E1101
    