from django.contrib import admin
from Home.models import Post


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


make_published.short_description = "Mark selected stories as published"


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

admin.site.register(Post, PostAdmin)