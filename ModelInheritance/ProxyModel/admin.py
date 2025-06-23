from django.contrib import admin
from .models import ExamCenter, MyExamCenter
# Register your models here.

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ('cname', 'address')
    
@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ('cname', 'address')