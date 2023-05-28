from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_cooker', 'is_customer', 'userprofile',
                  'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            email=validated_data.get('email'),
            is_cooker=validated_data.get('is_cooker'),
            is_customer=validated_data.get('is_customer')
        )
        user.save()
        return user
