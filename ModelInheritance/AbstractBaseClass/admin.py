from django.contrib import admin
from .models import CommonFeilds, Student, Teacher, PTStaff

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','name','age','phone_number','address')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id','name','age','email','phone_number','address')

@admin.register(PTStaff)
class PTStaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id','name','age','email','phone_number')