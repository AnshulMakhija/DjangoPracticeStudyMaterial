from django.shortcuts import render
from .forms import UserRegistration

# Create your views here.
def userform(request):
    obj = UserRegistration()
    return render(request, 'feilds/userform.html', {'form': obj})
