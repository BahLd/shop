from django.contrib import admin
from django.contrib.auth.models import User    
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')
    
admin.site.unregister(User) 
admin.site.register(User, UserAdmin)