from django.db import models
from django.contrib.auth.models import User
import PIL
from django.core.files.base import ContentFile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    gender = models.CharField(max_length=20, blank=True, default='unknown')
    age = models.CharField(max_length=20, blank=True, default='unknown')
    city = models.CharField(max_length=100, blank=True, default='unknown')
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/default_avatar.jpg')


class ResetPasswordModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code_checked = models.BooleanField(default=False, blank=True)
    code_send = models.BooleanField(default=False, blank=True)
    code = models.IntegerField(blank=True, default=0)
    limit = models.IntegerField(blank=True, default=0)


class ForgetPasswordCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(blank=True, max_length=32)
