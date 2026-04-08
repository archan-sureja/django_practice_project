from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import FormView, View , ListView , DetailView
from django.utils import timezone
from main_app.forms import LoginForm
from main_app.models import Job
from main_app.file_handling import ValidationUploadHandler
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

class RoleCheckMixin:
    role = None # role must be set in child class
    def dispatch(self, request, *args, **kwargs):
        if request.user.role != self.role:
            return HttpResponseForbidden("You are not authorized to access this page")
        return super().dispatch(request, *args, **kwargs)


