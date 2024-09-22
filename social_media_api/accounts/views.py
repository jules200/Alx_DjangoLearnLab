from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from accounts.serializers import CustomUserSerializer
from django.shortcuts import get_object_or_404

generics.GenericAPIView, permissions.IsAuthenticated
class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = CustomUser.objects.all()
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.follow(user_to_follow)
        return Response({'status': 'followed'}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({'status': 'unfollowed'}, status=status.HTTP_200_OK)