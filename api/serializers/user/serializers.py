from rest_framework import serializers

from models_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'balance',
            'color',
            'is_sleep',
            'is_active',
            'is_walk'
        )


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )
