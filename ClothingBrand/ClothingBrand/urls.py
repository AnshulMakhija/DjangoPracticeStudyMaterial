"""
URL configuration for ClothingBrand project.

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
from django.urls import path, include
from application import views
import application2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_application_fun1/', views.function1),
    path('view_application_fun2/', views.function2),
    path('view_application_fun3/', views.function3),
    path('view_application_fun4/', views.function4),
    path('application2/', include('application2.urls')),
    path('home/', views.render_request),
    path('UserData/', include('application.urls')),
]
