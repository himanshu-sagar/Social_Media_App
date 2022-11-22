from django.urls import include, path
from .views import FollowView, UnfollowView, UserConnectionDetailView

urlpatterns = [
    path('follow/<str:pk>', FollowView.as_view(), name='follow'),
    path('unfollow/<str:pk>', UnfollowView.as_view(), name='unfollow'),
    path('user', UserConnectionDetailView.as_view(), name='user'),
]
