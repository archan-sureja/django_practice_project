
from django.http import HttpRequest , HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
class MaintenanceModeMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        self.maintenance_mode = settings.MAINTENANCE_MODE

    def __call__(self,request : HttpRequest):
        if self.maintenance_mode and not request.user.is_staff and not request.path.startswith("/admin/"):
            return HttpResponse("Site is under maintenance. Please check back later.",status=503)
        response = self.get_response(request)
        return response