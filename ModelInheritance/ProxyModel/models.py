from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    cname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True