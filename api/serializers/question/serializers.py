from rest_framework import serializers

from api.serializers.answer.serializers import AnswerSerializer
from models_app.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'title',
            'answers',
        )
