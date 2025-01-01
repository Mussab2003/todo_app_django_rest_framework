from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    email_address = serializers.EmailField()
    password = serializers.CharField(max_length = 15)
    username = serializers.CharField(max_length = 50)

class LoginSerializer(serializers.Serializer):
    email_address = serializers.EmailField()
    password = serializers.CharField(max_length = 15)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at']
    

class TaskSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField()
    class Meta:
        model = Task
        exclude = ['status']

    def get_current_status(self, obj):
        return obj.current_status

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'due_date']


