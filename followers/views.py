from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from .models import Follower
from .serializers import FollowerSerializer
"""
class FollowerView(generics.CreateAPIView, generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
"""


class FollowView(views.APIView):
    def post(self, request, pk):
        user = request.user
        query = Follower.objects.filter(followed_user_id=pk, followed_by_user_id=user.id)
        if query.exists():
            return Response({"error": "Already Following the User"}, status=status.HTTP_409_CONFLICT)
        data = {"followed_user_id": pk, "followed_by_user_id": user.id}
        serializer = FollowerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnfollowView(views.APIView):
    def post(self, request, pk):
        user = request.user
        query = Follower.objects.filter(followed_user_id=pk, followed_by_user_id=user.id)
        if query.exists():
            query.delete()
            return Response({"message": "Follower Removed Successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Can not unfollow, have Not followed the user"}, status=status.HTTP_404_NOT_FOUND)


class UserConnectionDetailView(views.APIView):
    def get(self, request):
        user = request.user
        followers_query = Follower.objects.filter(followed_user_id=user.id).count()
        following_query = Follower.objects.filter(followed_by_user_id=user.id).count()
        data = {"username": user.username, "followers": followers_query, "following": following_query}

        return Response(data=data, status=status.HTTP_200_OK)
