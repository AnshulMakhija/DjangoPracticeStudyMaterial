from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
class Student(ExamCenter):
    name = models.CharField(max_length=255)
    rollno = models.CharField(max_length=255)