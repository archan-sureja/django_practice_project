from django.shortcuts import render,redirect
from django.http import HttpRequest , HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import SignUpFormRecruiter, SignUpFormApplicant , LoginForm


def sign_up_recruiter(request: HttpRequest):
    if request.method == "POST":
        form = SignUpFormRecruiter(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "REC"
            user.save()
            user.recruiter_profile.company = form.cleaned_data.get("company")
            user.recruiter_profile.experience = form.cleaned_data.get("experience")
            user.recruiter_profile.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"Signed up successfully")
            return redirect("dashboard")
    else:
        form = SignUpFormRecruiter()
    return render(request,"auth/sign_up_recruiter.html",{"form":form})
    

def sign_up_applicant(request: HttpRequest):
    if request.method == "POST":
        form = SignUpFormApplicant(request.POST,request.FILES)
        if form.is_valid(): #if using ModelForm then this will run DB Query to check constraints 
            user = form.save(commit=False)
            user.role = "APP"
            user.save()
            user.applicant_profile.resume = form.cleaned_data.get("resume")
            user.applicant_profile.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user =authenticate(request,username=username,password=password) #Db query to authenticate 
            login(request,user)
            messages.success(request,"Signed up successfully")
            return redirect("dashboard")
    else:
        form = SignUpFormApplicant()
    return render(request,"auth/sign_up_applicant.html",{"form":form})

def login_view(request: HttpRequest):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user) # creates session for user and adds user id to session data
                if user.role == "REC":
                    return redirect("recruiter_dashboard")
                return redirect("applicant_dashboard")
            form.add_error(None,"Invalid username or password") # non field error , by default rendered at top of form
            return render(request,"auth/login.html",{"form":form}) 
    return render(request,"auth/login.html",{"form":LoginForm()})

@login_required(login_url="login",redirect_field_name=None) # if user is not logged in then redirect to login page
def dashboard(request: HttpRequest):
    if request.user.role == "REC":
        return render(request,"dashboard.html",{"user_type":"Recruiter"})
    return render(request,"dashboard.html",{"user_type":"Applicant"})

def logout_view(request: HttpRequest):
    logout(request) # removes user id from session data and flushes session
    # messages.success(request,"Logged out successfully")
    return redirect("login")