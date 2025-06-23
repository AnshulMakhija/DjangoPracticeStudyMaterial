from django import forms
from .models import User
from django.core import validators

class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'render_value': True,'class': 'form-control', 'placeholder': 'Enter your password'}),
        }
        error_messages = {
            'name': {
                'required': 'Name is required.',
                'max_length': 'Name cannot exceed 100 characters.',
            },
            'email': {
                'required': 'Email is required.',
                'invalid': 'Enter a valid email address.',
            },
            'password': {
                'required': 'Password is required.',
                'max_length': 'Password cannot exceed 100 characters.',
            },
        }