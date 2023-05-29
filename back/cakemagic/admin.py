from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_cooker', 'is_customer')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'is_cooker', 'is_customer')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'email')}),
        ('Доступы', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'is_cooker', 'is_customer', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser',
                'is_cooker', 'is_customer', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('id',)
    pass


admin.site.register(User, CustomUserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'city')
