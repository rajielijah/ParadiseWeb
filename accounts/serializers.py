from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer


class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        email = self.validated_data['email']
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise serializers.ValidationError(
                'This e-mail has already been used by another user'
            )

        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], password=validated_data['password'])
        user.first_name = self.validated_data['first_name']
        user.last_name = self.validated_data['last_name']
        user.save()
        return user
# Login Serializer


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            'Incorrect Username or Password!')
