from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegister
from .models import User

# Create your views here.
#adding new user and showing all users
def add_show(request):
    if request.method == 'POST':
        obj = UserRegister(request.POST)
        if obj.is_valid():
            # obj.save() # Save the form data to the database
            # Another way to save the form data cleaned_data
            nm = obj.cleaned_data['name']
            em = obj.cleaned_data['email']
            pw = obj.cleaned_data['password']
            user = User(name=nm, email=em, password=pw)
            user.save()
            obj = UserRegister() # Reset the form after saving
    else:
        obj = UserRegister()
    users = User.objects.all()
    return render(request,'curd_app/add_show.html',{'form': obj, 'user': users})


# Function to delete a user
def delete_user(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect('/')
    
# Function to update a user
def update_user(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        fm = UserRegister(request.POST, instance=obj)
        if fm.is_valid():
            fm.save()
    
    else:
        obj = User.objects.get(pk=id)
        fm = UserRegister(instance=obj)
        
    return render(request, 'curd_app/update_user.html', {'form': fm})