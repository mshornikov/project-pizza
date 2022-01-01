from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

UserModel = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user( username=validated_data['username'], password=validated_data['password'],)
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'phone', 'date_of_birth',  'password')