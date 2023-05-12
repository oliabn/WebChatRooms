import json
import datetime

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.room_group_name = "group_chat_gfg"
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(self.room_group_name,
                                            {"type": "sendMessage",
                                             "message": message,
                                             "username": username, })

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        date = str(datetime.date.today())
        await self.send(text_data=json.dumps({"message": message,
                                              "username": username,
                                              "date": date, }))
