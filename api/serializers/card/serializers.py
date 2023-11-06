from rest_framework import serializers

from models_app.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = (
            'id',
            'title',
            'cost',
            'image',
            'position',
            'type',
        )
