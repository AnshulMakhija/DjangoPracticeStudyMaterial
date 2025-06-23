from django.urls import path
from .views import send_email_view

urlpatterns = [
    path('sendemail/', send_email_view, name="send-email"),
]
