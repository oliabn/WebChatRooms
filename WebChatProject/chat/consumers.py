import json
import datetime

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    """Web socket event consumer"""
    async def connect(self):
        """Connect a user to chat"""

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join user to an existing room group or a newly created one
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)

        # get user from scope
        self.user = self.scope['user']
        # get message history data to send it for connecting user
        message_history = await self.get_message_history()

        # accept user connection
        await self.accept()

        # send messages from message_history to user
        for msg in message_history:
            await self.send(text_data=json.dumps(msg))

    async def disconnect(self, close_code):
        """Leave the room group"""

        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        """Receive message from WebSocket"""

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        # save message to Message table
        await self.save_message_to_db(message=message)

        # Sends an event to a group
        # event has "type": "sendMessage", where sendMessage is function below
        await self.channel_layer.group_send(self.room_group_name,
                                            {"type": "send_message",
                                             "message": message,
                                             "username": username, })

    async def send_message(self, event):
        """Receive message from the room group Event.
        It will be invoked for consumers that receive the event"""

        message = event["message"]
        username = event["username"]
        date = str(datetime.date.today())

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,
                                              "username": username,
                                              "date": date, }))

    @database_sync_to_async
    def save_message_to_db(self, message):
        """Save message to table Message"""

        Message.objects.create(user=self.user,
                               text=message,
                               room=Room.objects.get(name=self.room_name))

    @database_sync_to_async
    def get_message_history(self):
        """Get messages of room group from the table Message.
        Return a list of dictionaries with messages,
        usernames, and dates:
        [{"message": msg1.text, "username": msg1.user.username, "date": str(msg1.timestamp)},
        {"message": msg2.text, "username": msg2.user.username, "date": str(msg2.timestamp)},
        ...]"""

        messages = Message.objects.all().filter(room__name=self.room_name)
        message_history = []
        for msg in messages:
            message_history.append({
                "message": msg.text,
                "username": msg.user.username,
                "date": str(msg.timestamp)
            })

        return message_history
