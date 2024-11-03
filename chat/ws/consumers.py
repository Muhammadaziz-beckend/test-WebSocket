# myapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Принять соединение

    async def disconnect(self, close_code):
        pass  # Здесь можно добавить логику при отключении

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправляем обратно то же сообщение
        await self.send(text_data=json.dumps({
            'message': message
        }))
