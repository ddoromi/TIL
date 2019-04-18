from django.db import models


class Posting(models.Model):
    title = models.CharField(max_length=200, default='')
    

class Comment(models.Model):
    content = models.CharField(max_length=200, default='')