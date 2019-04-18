from django.db import models


class User(models.Model):
    email = models.CharField(max_length=30, default='', unique=True)
    password = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    last_name = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=50, default='')