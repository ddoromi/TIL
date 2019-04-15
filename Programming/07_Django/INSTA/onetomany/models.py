from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class MegazineArticle(TimeStampedModel, TitleDescriptionModel):
    content = models.TextField()


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=50, default='')


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')


class Chapter(TitleDescriptionModel, TimeStampedModel):
     book = models.ForeignKey(Book, on_delete=models.CASCADE)

