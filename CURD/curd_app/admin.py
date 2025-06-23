from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
    search_fields = ('name', 'email')
    list_filter = ('name',)
    ordering = ('id',)
    list_per_page = 10