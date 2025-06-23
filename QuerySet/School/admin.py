from django.contrib import admin
from .models import student,teacher 

# Register your models here.
@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'age', 'marks','standard')

@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id','name','age', 'total_subject', 'standard')