from django.contrib import admin
from .models import ResetPasswordModel

class Profiles(admin.ModelAdmin):
    list_display = ['user', 'code_checked', 'code_send', 'code']

admin.site.register(ResetPasswordModel, Profiles)
