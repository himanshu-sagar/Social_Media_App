from django.urls import path
from .views import PostView, LikeView, UnlikeView

urlpatterns = [
    path('posts', PostView.as_view(), name="create_post"),
    path('posts/<str:pk>', PostView.as_view(), name="delete_post"),
    path('like/<str:pk>', LikeView.as_view(), name="like_post"),
    path('unlike/<str:pk>', UnlikeView.as_view(), name="unlike_post")
]
