from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) # Cascade: if user is deleted, student is also deleted
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    
