from django.contrib.auth import get_user_model
from django.contrib import admin

@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    pass
