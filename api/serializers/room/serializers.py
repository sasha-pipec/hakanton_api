from rest_framework import serializers

from models_app.models import Room


class RoomSerializer(serializers.ModelSerializer):
    count_players_now = serializers.SerializerMethodField()

    def get_count_players_now(self, obj):
        return obj.users.all().count()

    class Meta:
        model = Room
        fields = (
            'id',
            'title',
            'count_players',
            'count_players_now',
        )
