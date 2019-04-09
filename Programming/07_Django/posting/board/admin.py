from django.contrib import admin
from .models import Posting, Comment
# Register your models here.

class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_link = ('id', 'title')


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'posting', 'content', 'created_at', 'updated_at')
    list_display_link = ('id', 'content')


admin.site.register(Posting, PostingModelAdmin)
admin.site.register(Comment, CommentModelAdmin)