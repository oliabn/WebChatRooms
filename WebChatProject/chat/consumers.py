import json
import datetime

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join to room group
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        """Receive message from WebSocket"""

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        # Sends an event to a group
        # event has "type": "sendMessage", where sendMessage is function below
        await self.channel_layer.group_send(self.room_group_name,
                                            {"type": "sendMessage",
                                             "message": message,
                                             "username": username, })

    async def sendMessage(self, event):
        """Receive message from the room group Event.
        It will be invoked for consumers that receive the event"""

        message = event["message"]
        username = event["username"]
        date = str(datetime.date.today())

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,
                                              "username": username,
                                              "date": date, }))
