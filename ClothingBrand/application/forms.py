from django import forms
from .models import Employee

class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100,error_messages={'required': 'Enter your username'})
    #username = forms.CharField(error_value='Ram') # Default value if not provided
    first_name = forms.CharField(label="First Name", max_length=50, required=True)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid', 'first_name', 'username', 'email', 'password']