import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import *

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = 'chat_%s' % self.game_name

        # Join game
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave game
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )
    
    # Receive game data
    async def receive(self, game_data):
        data = json.loads(game_data)
        player = data['player']
        shuriken = data['shuriken']

        await self.save_player(player)
        await self.save_shuriken(shuriken)

        # Send data to game group
        await self.channel_layer.group_send(
            self.game_group_name,
            {
                'type': 'game_data',
                'player': player,
                'shuriken': shuriken
            }
        )
    
    # Receive message from room group
    async def game_data(self, event):
        player = event['player']
        shuriken = event['shuriken']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'player': player,
            'shuriken': shuriken
        }))

    # Saving to Redis
    @sync_to_async
    def save_player(self, player):
        Player.objects.create(username=player.username, posX=player.posX, posY=player.posY)

    @sync_to_async
    def save_shuriken(self, shuriken):
        Shuriken.objects.create(playerName=shuriken.playerName, posX=shuriken.posX, posY=shuriken.posY)
