from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
