import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SignalingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 🔐 Vérifie si l'utilisateur est connecté
        user = self.scope["user"]
        if not user.is_authenticated:
            await self.close()  # Refuse la connexion
            return

        # ✅ Connexion autorisée
        self.room_code  = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f"signaling_{self.room_code}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'signal.message',
                'text': text_data,
            }
        )

    async def signal_message(self, event):
        await self.send(text_data=event['text'])
