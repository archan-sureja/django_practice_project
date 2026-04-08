
import logging

from django.http import HttpRequest , HttpResponse
from django.conf import settings
from main_app.file_handling import ValidationUploadHandler
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


class CustomFileUploadHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("[MIDDLEWARE] Adding custom upload handler")
        request.upload_handlers.insert(0, ValidationUploadHandler(request))
        response = self.get_response(request)
        return response

logger = logging.getLogger(__name__)
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'{request.method} {request.path}')
        
        response = self.get_response(request)
        
        logger.info(f'Response status: {response.status_code}')
        return response