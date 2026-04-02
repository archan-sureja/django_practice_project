from django.views import View 
from django.views.generic import ListView,CreateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from main_app.forms import SignUpFormApplicant
from main_app.models import ApplicantProfile, Application
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
    role = "APP"
    role_check_fail_url = "login"
    model = Application 
    login_url = "/login/"
    template_name = "applicant/dashboard.html"
    context_object_name = "applications"
    paginate_by = 10
    ordering = ["-applied_at"]

    def get_queryset(self):
        return Application.objects.select_related('job').filter(applicant=self.request.user,job__is_active=True) #pylint: disable=E1101


