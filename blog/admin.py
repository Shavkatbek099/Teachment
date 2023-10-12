from django.contrib import admin
from .models import Post, Student


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'status', 'publish']
    list_filter = ['author', 'status', 'created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'age']
