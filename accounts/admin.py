from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "pfp",
        "max_education",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            "fields": ("pfp", "max_education")
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
        ('Additional Info', {
            'fields': ('pfp', 'max_education'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
