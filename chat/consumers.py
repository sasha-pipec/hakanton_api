import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class WSChatRoomView(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'post_for_room_' + str(self.scope['url_route']['kwargs']['id'])
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(
            self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        )

    def receive(self, **kwargs):
        data = json.loads(kwargs['text_data'])
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                **data
            }
        )

    def room_step(self, event):
        async_to_sync(
            self.send(text_data=json.dumps({
                **event
            }))
        )

    def send_color(self, event):
        async_to_sync(
            self.send(text_data=json.dumps({
                **event
            }))
        )

    def connect_to_room(self, event):
        async_to_sync(
            self.send(text_data=json.dumps({
                **event,
                'count_players': int(event['count_players']) + 1
            }))
        )

    def disconnect_to_room(self, event):
        async_to_sync(
            self.send(text_data=json.dumps({
                **event,
                'count_players': int(event['count_players']) - 1
            }))
        )

    def message(self, event):
        async_to_sync(
            self.send(text_data=json.dumps({
                **event
            }))
        )
