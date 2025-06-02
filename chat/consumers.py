# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SignalingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Si vous utilisez JWT (ou session), vérifiez l’authentification ici :
        user = self.scope["user"]
        if not user.is_authenticated:
            await self.close()
            return

        self.room_code  = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f"signaling_{self.room_code}"

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        """
        text_data est la chaîne JSON reçue du frontend,
        par ex. '{"type":"offer","sdp":{…}}' ou '{"type":"ice-candidate","candidate":{…}}'
        """
        # On transmet directement ce texte à tous les membres du groupe
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'signal_message',   # correspond à la méthode signal_message()
                'text': text_data,
            }
        )

    async def signal_message(self, event):
        """
        Channels appellera cette méthode quand un message de type 'signal_message'
        est group_send()→émit. On renvoie alors le JSON tel quel au client WebSocket.
        """
        await self.send(text_data=event['text'])
