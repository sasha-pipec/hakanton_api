from rest_framework import serializers

from models_app.models import Room


class RoomSerializer(serializers.ModelSerializer):
    count_players_now = serializers.SerializerMethodField()
    in_room = serializers.SerializerMethodField()

    def get_count_players_now(self, obj):
        return obj.users.all().count()

    def get_in_room(self, obj):
        return obj.users.filter(id=self.context['user'].id).exists()

    class Meta:
        model = Room
        fields = (
            'id',
            'title',
            'count_players',
            'count_players_now',
            'in_room',
        )
