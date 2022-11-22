from django.contrib import admin
from .models import Reaction, Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'created_at']


class ReactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'liked_by', 'created_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'comment_by','comment', 'created_at']


admin.site.register(Post, PostAdmin)
admin.site.register(Reaction, ReactionAdmin)
admin.site.register(Comment, CommentAdmin)