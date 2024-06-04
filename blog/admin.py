from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status',)
    search_fields = ['title', 'content']
    list_display = ('title', 'status', 'created_on')


admin.site.register(Category)

admin.site.register(Comment)