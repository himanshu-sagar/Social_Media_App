from rest_framework import views, status
from rest_framework.response import Response
from .serializers import PostSerializer, ReactionSerializer
from .models import Post, Reaction


class PostView(views.APIView):
    def post(self, request):
        user = request.user
        request.data["user"] = user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        query = Post.objects.filter(user=user.id, id=pk)
        if query.exists():
            query.delete()
            return Response({"message": "Post Deleted Successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "No Post Found with this id for this user"}, status=status.HTTP_404_NOT_FOUND)


class LikeView(views.APIView):
    def post(self, request, pk):
        user = request.user
        query = Reaction.objects.filter(post=pk, liked_by=user.id)
        if query.exists():
            return Response({"error": "Already liked by user"}, status=status.HTTP_409_CONFLICT)
        data = {"post": pk, "liked_by": user.id}
        serializer = ReactionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnlikeView(views.APIView):
    def post(self, request, pk):
        user = request.user
        query = Reaction.objects.filter(post=pk, liked_by=user.id)
        if query.exists():
            query.delete()
            return Response({"message": "Post Unliked Successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Can not like, have not liked the user"}, status=status.HTTP_404_NOT_FOUND)
