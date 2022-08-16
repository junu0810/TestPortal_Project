from dataclasses import field
from statistics import mode
from .models import User
from rest_framework import serializers

class BaseUserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

    def create(self , validated_data):
        return User.objects.create(**validated_data)

    def update(self , instance , validated_data):
        instance.title = validated_data.get('email' , instance.email)
        instance.save()
        return instance
