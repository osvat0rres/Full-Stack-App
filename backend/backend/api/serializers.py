from django.contrib.auth.models import User 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        #no one can read the password
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.Objects.create_user(**validated_data)
        return user    