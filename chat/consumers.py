import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class WSChatRoomView(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'post_for_room_' + str(self.scope['url_route']['kwargs']['id'])
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, **kwargs):
        data = json.loads(kwargs['text_data'])
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'message',
                'message': data.get('message'),
                'username': data.get('username'),
            }
        )

    async def message(self, event):
        await self.send_json(event, close=False)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
