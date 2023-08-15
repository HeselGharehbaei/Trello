from django.contrib import admin
from .models import User
from workspaces.models import Workspace
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'email', 'date_joined',)
    list_filter = ('is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name','image', 'email',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff'),
            'classes': ('collapse',)
        }),
        (_("Date Information"), {
            'fields': ('date_joined',),
            'classes': ('collapse',)
        }),
    )
    

