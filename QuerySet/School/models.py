from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True, null=False)
    age = models.IntegerField()
    marks = models.IntegerField()
    standard = models.IntegerField()
    
class teacher(models.Model):
    name = models.CharField(max_length=100)
    teacher_id = models.IntegerField(unique=True, null=False)
    age = models.IntegerField()
    total_subject = models.IntegerField()
    standard = models.IntegerField()