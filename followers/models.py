from django.db import models
from authentication.models import User


class Follower(models.Model):

    followed_user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name="followed")
    followed_by_user_id = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE, related_name="followed_by")
    created_at = models.DateTimeField(auto_now_add=True)
