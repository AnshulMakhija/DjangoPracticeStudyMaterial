from django import forms
from .models import User

class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'  # This will include all fields from the User model
        # fields = ['firstname', 'lastname', 'username', 'email', 'password']
        exclude = ['password']  # Exclude the password field for security reasons