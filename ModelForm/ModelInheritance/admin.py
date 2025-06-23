from django.contrib import admin
from .models import StudentTeacher

@admin.register(StudentTeacher)
class StudentTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'student_name', 'teacher_age', 'student_age', 'teacher_email', 'student_email')
    search_fields = ('teacher_name', 'student_name')

# Register your models here.
