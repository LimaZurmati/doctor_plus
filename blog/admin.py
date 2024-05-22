from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)