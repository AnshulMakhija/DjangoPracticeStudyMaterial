from django.db import models

# Create your models here.
class CommonFeilds(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    class Meta:
        abstract = True
        
class Student(CommonFeilds):
    student_id = models.CharField(max_length=20)
    email = None
    
class Teacher(CommonFeilds):
    teacher_id = models.CharField(max_length=20)
    
class PTStaff(CommonFeilds):
    staff_id = models.CharField(max_length=20)
    address = None
        

