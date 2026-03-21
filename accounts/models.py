from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", default='default.jpg')
    bio = models.CharField(max_length=150, null=True, blank=True)