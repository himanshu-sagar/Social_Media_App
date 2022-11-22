from django.contrib import admin
from .models import Reaction, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'created_at']


class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'liked_by', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Reaction, ReactionAdmin)