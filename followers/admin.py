from django.contrib import admin
from .models import Follower
# Register your models here.


class FollowerAdmin(admin.ModelAdmin):
    list_display = ['id', 'followed_by_user_id', 'followed_user_id', 'created_at']


admin.site.register(Follower, FollowerAdmin)