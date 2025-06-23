from django.urls import path, include
from . import views

urlpatterns = [
    path('Userdata/', views.user_data),
    path('showform/', views.show_form),
    path('success/', views.thankyou),
    path('showform_employee/', views.show_form_employee),
]
