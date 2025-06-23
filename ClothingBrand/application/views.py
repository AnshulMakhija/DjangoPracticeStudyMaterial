from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from application.models import User
from .forms import UserForm
from .models import User, Employee

# Create your views here.

def function1(request):
    return HttpResponse("Hello Everyone this is our first function")

def function2(request):
    return HttpResponse(" <h1> Hello Everyone this is our second function </h1> ")

def function3(request):
    a = 10+10
    return HttpResponse(a)

def function4(request):
    a = 10
    return HttpResponse("Hey this is number "+ str(a))

def render_request(request):
    return render(request, 'home.html')

def user_data(request):
    user_d = User.objects.all()
    return render(request, 'user_data.html', {'user_data': user_d})

def thankyou(request):
    return render(request, 'user_form_success.html')

def show_form(request):
    
    if request.method == 'POST':
        obj = UserForm(request.POST)
        if obj.is_valid():
            print("form is valid")
            print("Name: ", obj.cleaned_data['username'])
            first_name = obj.cleaned_data['first_name']
            user_name = obj.cleaned_data['username']
            email = obj.cleaned_data['email']
            password = obj.cleaned_data['password']
            print("Email: ", obj.cleaned_data['email'])
            #return render(request, 'user_form_success.html', {'name': user_name})
            registered_user = User(username=user_name,first_name= first_name, email=email, password=password)
            registered_user.save()
            return HttpResponseRedirect('/UserData/success/')

    else:
        obj = UserForm(auto_id=True,label_suffix=' ')
        #label_suffix is used to add a colon (space,:,-,:-) after the label
        #obj.order_fields(field_order=['email', 'username', 'password'])
        return render(request, 'user_form.html', {'form': obj})
    
    
def show_form_employee(request):
    
    if request.method == 'POST':
        obj = UserForm(request.POST)
        if obj.is_valid():
            print("form is valid")
            print("Name: ", obj.cleaned_data['username'])
            first_name = obj.cleaned_data['first_name']
            user_name = obj.cleaned_data['username']
            email = obj.cleaned_data['email']
            password = obj.cleaned_data['password']
            print("Email: ", obj.cleaned_data['email'])
            #return render(request, 'user_form_success.html', {'name': user_name})
            registered_user = Employee(username=user_name,first_name= first_name, email=email, password=password)
            registered_user.save()
            return HttpResponseRedirect('/UserData/success/')

    else:
        obj = UserForm(auto_id=True,label_suffix=' ')
        #label_suffix is used to add a colon (space,:,-,:-) after the label
        #obj.order_fields(field_order=['email', 'username', 'password'])
        return render(request, 'user_form.html', {'form': obj})
    
    