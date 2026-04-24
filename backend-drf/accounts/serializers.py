from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # User.objects.create = save the passoword in plain text so it will need to be hashed
        # User.objects.create_user = automatically hash the password
        # You should use **validated_date only if you have required fields that is not important infromation
        # as it encapsulates all fields
        user = User.objects.create_user(**validated_data)
        return user