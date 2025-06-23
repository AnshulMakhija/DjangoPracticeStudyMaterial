from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import GeeksModel

class GeeksCreate(CreateView):
    model = GeeksModel
    fields = ['title', 'description']
    template_name = 'classApp/geeksmodel_form.html'
    success_url = '/'
    
class GeeksList(ListView):
    model = GeeksModel
    template_name = 'classApp/geeksmodel_list.html'
    context_object_name = 'geeks_list'

class GeeksDetailView(DetailView):
    model = GeeksModel
    template_name = 'classApp/geeksmodel_detail.html'
    
class GeeksUpdateView(UpdateView):
    model = GeeksModel
    fields = [
        "title",
        "description"
    ]
    success_url ="/"
    
class GeeksDeleteView(DeleteView):
    model = GeeksModel
    success_url ="/"