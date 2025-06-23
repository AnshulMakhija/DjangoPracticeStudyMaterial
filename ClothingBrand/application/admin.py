from django.contrib import admin
from application.models import User

@admin.register(User)

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('empid', 'first_name', 'username', 'email')
    search_fields = ('first_name', 'username', 'email')

#admin.site.register(User, UserAdmin)

