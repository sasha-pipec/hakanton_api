from rest_framework import serializers

from models_app.models import Card, UserCard


class CardSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()
    owner_id = serializers.SerializerMethodField()

    class Meta:
        model = Card
        fields = (
            'id',
            'owner_id',
            'title',
            'cost',
            'image',
            'position',
            'type',
            'color',
            'index',
        )

    def get_color(self, obj):
        try:
            return UserCard.objects.get(
                room_id=self.context['room_id'],
                card=obj,
            ).user.color
        except UserCard.DoesNotExist:
            return None

    def get_owner_id(self, obj):
        owner = UserCard.objects.filter(
            room_id=self.context['room_id'],
            card=obj,
        )
        if owner.exists():
            return owner.first().user.id
        return None
