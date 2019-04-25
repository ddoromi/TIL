from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


"""
1. $ django-admin startproject MY_PROJECT
2. $ django-admin startapp accounts
3. accounts/models.py => 아래 코드 작성
4. settings.py => INSTALED APPS => 'accounts'
5. AUTH_USER_MODEL = 'accounts.User'
"""


class User(AbstractUser):
    followings = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username
