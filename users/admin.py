from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'password', 'is_staff', 'is_active',)
    list_filter = ('email', 'name', 'password', 'liked_events', 'fav_tags', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password', 'liked_events', 'fav_tags',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'name', 'password', 'liked_events', 'fav_tags',)
    ordering = ('email', 'name', 'liked_events', 'fav_tags', 'password',)


admin.site.register(CustomUser, CustomUserAdmin)