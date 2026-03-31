from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpFormRecruiter, SignUpFormApplicant
from django.contrib.auth import authenticate, login
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
            return HttpResponse("Recruiter signed up successfully , Home page coming soon")
    else:
        form = SignUpFormRecruiter()
    return render(request,"auth/sign_up_recruiter.html",{"form":form})
    

def sign_up_applicant(request: HttpRequest):
    if request.method == "POST":
        form = SignUpFormApplicant(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "APP"
            user.save()
            user.applicant_profile.resume = form.cleaned_data.get("resume")
            user.applicant_profile.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            authenticate(request,username=username,password=password)
            login(request,user)
            print("DEBUG: Applicant form is valid")
            return HttpResponse("Applicant signed up successfully , Home page coming soon")
    else:
        form = SignUpFormApplicant()
    return render(request,"auth/sign_up_applicant.html",{"form":form})

