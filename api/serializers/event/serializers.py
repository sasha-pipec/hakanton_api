from rest_framework import serializers

from models_app.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'types',
        )
