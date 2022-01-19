from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('id', 'profile_of_user', 'address')