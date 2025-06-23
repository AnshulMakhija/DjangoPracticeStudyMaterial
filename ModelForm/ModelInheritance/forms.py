from django import forms
from .models import StudentTeacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentTeacher
        fields = ['student_name', 'student_age', 'student_email']
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model = StudentTeacher
        fields = ['teacher_name', 'teacher_age', 'teacher_email']
        
        