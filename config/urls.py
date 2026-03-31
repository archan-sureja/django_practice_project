"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from main_app.views import sign_up_applicant, sign_up_recruiter , login_view , dashboard , logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/recruiter/',sign_up_recruiter , name="sign_up_recruiter"),
    path('signup/applicant/',sign_up_applicant , name="sign_up_applicant"),
    # path('login/',login_view , name="login"), 
    path('login/',auth_views.LoginView.as_view(template_name="auth/login.html"),name="login"), # using built in login view of django which handles both get and post request for login 
    # default form : autheticationForm with username and password field and template : registration/login.html
    # settings required : LOGIN_REDIRECT_URL="/dashboard" and LOGOUT_REDIRECT_URL="/login" , where to redirect after login and logout respectively
    path('dashboard/', dashboard, name="dashboard"),
    # path('logout/', logout_view, name="logout")
    path('logout/', auth_views.LogoutView.as_view(), name="logout") # using built in logout view of django which handles logout functionality and then redirects to LOGOUT_REDIRECT_URL
]
