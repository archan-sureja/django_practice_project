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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from main_app.views import common_views, applicant_views, recruiter_views
import debug_toolbar



urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),

    path('admin/', admin.site.urls),

    path('signup/applicant/', applicant_views.SignupApplicant.as_view(), name='signup_applicant'),
    path('signup/recruiter/', recruiter_views.SignupRecruiter.as_view(), name='signup_recruiter'),
    path('login/',common_views.LoginView.as_view(), name='login'),

    path('applicant/jobs/<int:job_id>/update/<int:application_id>/', applicant_views.JobApplicationView.as_view(),{"action":"update"}, name='update_application'),
    path('applicant/dashboard/jobs/<int:job_id>/withdraw/<int:application_id>/', applicant_views.JobApplicationView.as_view(),{"action":"withdraw"}, name='withdraw_application'),
    path('applicant/dashboard/jobs/<int:job_id>/apply/', applicant_views.JobApplicationView.as_view(),{"action":"create"}, name='create_application'),

    path('applicant/dashboard/jobs/<int:job_id>/', applicant_views.ApplicantJobDetailView.as_view(), name='job_detail'),

    path('applicant/dashboard/applications/', applicant_views.ApplicantionListView.as_view(), name='applications'),

    path('applicant/dashboard/', applicant_views.ApplicantDashboard.as_view(), name='applicant_dashboard'),

    path('recruiter/dashboard/<int:job_id>/applications/',recruiter_views.JobWiseApplications.as_view(),name="job_wise_applications"),
    path('recruiter/dashboard/process/applications/<int:application_id>/',recruiter_views.ProcessApplication.as_view(),name="process_application"),
    path('recruiter/dashboard/jobs/create/', recruiter_views.CreateJob.as_view(), name='create_job'),
    path('recruiter/dashboard/jobs/<int:job_id>/edit/', recruiter_views.EditJob.as_view(), name='edit_job'),
    path('recruiter/dashboard/', recruiter_views.RecruiterDashboard.as_view(), name='recruiter_dashboard'),
    path('logout/',common_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:  # Only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)