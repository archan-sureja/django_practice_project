from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import FormView, View , ListView , DetailView
from django.utils import timezone
from main_app.forms import LoginForm
from main_app.models import Job
class LoginView(FormView):
    template_name = "auth/login.html"
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                if user.role == "REC":
                    return redirect("recruiter_dashboard")
                else:
                    return redirect("applicant_dashboard")
            else:
                messages.error(request, "Invalid username or password")
        return self.form_invalid(form)

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("login")


class JobListView(ListView):
    model = Job
    template_name = "common/job_list.html"
    context_object_name = "jobs"
    paginate_by = 10
    ordering = ["-posted_at"]

    def get_queryset(self):
        return Job.objects.filter(deadline__gte=timezone.localdate(),is_active=True) #pylint: disable=E1101

class JobDetailVew(DetailView):
    model = Job
    template_name = "common/job_detail.html"
    context_object_name = "job"

    def get_object(self, queryset = ...):
        return Job.objects.select_related("posted_by","company").get(pk=self.kwargs.get("pk")) #pylint: disable=E1101