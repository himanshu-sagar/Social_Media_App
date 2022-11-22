from django.db import models
from authentication.models import User


class Post(models.Model):
    user = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE, related_name="posted_by")
    title = models.CharField(max_length=250, null=False)
    description = models.CharField(max_length=3000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    liked_by = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE, related_name="user")
    post = models.ForeignKey(Post, to_field="id", on_delete=models.CASCADE, related_name="post")
    created_at = models.DateTimeField(auto_now_add=True)
