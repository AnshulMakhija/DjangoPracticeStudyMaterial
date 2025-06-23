from django.db import models

# Create your models here.

class StudentTeacher(models.Model):
    teacher_name = models.CharField(max_length=100, null = True, blank= True)
    student_name = models.CharField(max_length=100, null = True, blank= True)
    teacher_age = models.IntegerField( null = True, blank= True)
    student_age = models.IntegerField( null = True, blank= True)
    teacher_email = models.EmailField( null = True, blank= True)
    student_email = models.EmailField( null = True, blank= True)

    def __str__(self):
        return f'{self.teacher_name} - {self.student_name}'
