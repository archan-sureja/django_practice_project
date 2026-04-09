from django.urls import path
from . import consumers 

websocket_urlpatterns = [ 
    path("notify/applicant/<int:user_id>/",consumers.ApplicantNotifier.as_asgi())
]