from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from profiles.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email',]
            )
        ]

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.save()
        return user
    
    def	save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            password = self.validated_data['password'],
        )
        user.save()
        return user