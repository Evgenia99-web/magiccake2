from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password


class RegistrationView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Please provide all required fields.'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=400)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            userprofile = get_object_or_404(UserProfile, user=user)
            profile_data = UserProfileSerializer(userprofile).data
            user_data = UserSerializer(user).data
            user_data['userprofile'] = profile_data

            token, created = Token.objects.get_or_create(user=user)
            user_data['token'] = token.key
            return Response(user_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        # Retrieve related  info
        userprofile = get_object_or_404(UserProfile, user=user)
        profile_data = UserProfileSerializer(userprofile).data

        # Serialize and return user data with related artist info
        user_data = UserSerializer(user).data
        user_data['userprofile'] = profile_data
        user_data['token'] = token.key

        return Response(user_data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # check if username or password is being updated
        if 'username' in serializer.validated_data:
            # set new username
            serializer.instance.username = serializer.validated_data['username']
        if 'password' in serializer.validated_data:
            # set new password (hashed)
            serializer.instance.password = make_password(serializer.validated_data['password'])
        # save changes
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, *args, **kwargs):
        # check if user is updating their own profile
        if request.user.id != int(kwargs['pk']):
            return Response({'error': 'Not authorized to update this user.'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)
