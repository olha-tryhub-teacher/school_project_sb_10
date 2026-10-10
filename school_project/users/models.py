from django.db import models
# Create your models here.

from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ("user", "Пользователь"),
        ("Moderator", "Модератор"),
        ("admin", "Адміністратор"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    created_at = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="avatarsmedia/", blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default="user")