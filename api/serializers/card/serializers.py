from rest_framework import serializers

from models_app.models import Card, UserCard


class CardSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = (
            'id',
            'title',
            'cost',
            'image',
            'position',
            'type',
            'color',
        )

    def get_color(self, obj):
        try:
            return UserCard.objects.get(
                room_id=self.context['room_id'],
                card=obj,
            ).user.color
        except UserCard.DoesNotExist:
            return None
