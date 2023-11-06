from rest_framework import serializers

from models_app.models import Answer


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = (
            'id',
            'title',
            'is_correct',
        )
