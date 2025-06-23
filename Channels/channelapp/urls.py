#from django.conf.urls import url
from . import views
from django.urls import path

"""urlpatterns = [
    url(r'^$', views.index, name="index"),
]"""

urlpatterns = [
    path(r'^$', views.index, name="index"),
]