import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatRoom, Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")
        
        if action == "send":
            message_text = data.get("message", "")
            user = self.scope["user"]

            # 1. Save to DB
            message = await self.create_message(self.room_id, user, message_text)
            
            # 2. Broadcast to EVERYONE in the group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_broadcast", # This must match the method name below
                    "action": "receive",
                    "sender": user.username,
                    "content": message_text,
                    "timestamp": message.timestamp.strftime("%H:%M")
                }
            )

    # 3. This method MUST exist to actually send the data to the browser
    async def chat_broadcast(self, event):
        await self.send(text_data=json.dumps({
            "action": event["action"],
            "sender": event["sender"],
            "content": event["content"],
            "timestamp": event["timestamp"]
        }))

    @database_sync_to_async
    def create_message(self, room_id, user, text):
        # Use get_object_or_404 style logic to ensure the room exists
        try:
            room = ChatRoom.objects.get(id=room_id)
            return Message.objects.create(room=room, sender=user, text=text)
        except ChatRoom.DoesNotExist:
            return None