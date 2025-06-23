from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully!')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'signup/signup.html', {'form': fm})

#Login 
def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'signup/login.html', {'form': fm})

#profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'signup/profile.html',{'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#forgot password
def forgot_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)  # Important to keep the user logged in after password change
                messages.success(request, 'Password changed successfully!')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'signup/forgot_password.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')