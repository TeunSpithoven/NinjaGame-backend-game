import json
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import *

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = 'game_%s' % self.game_name

        # Join game
        await self.channel_layer.group_add(self.game_group_name, self.channel_name)
        # await self.save_game(self.game_name)

        await self.accept()
        self.send(text_data="[Welcome %s]" % self.game_name)
        self.send(text_data="connected to websocket!")
    
    async def disconnect(self, close_code):
        # Leave game
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )
    
    # Receive game data
    async def receive(self, text_data):
        data = json.loads(text_data)
        player = data['player']
        print(player)
        shuriken = data['shuriken']
        print(shuriken)

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
        await self.send(game_data=json.dumps({
            'player': player,
            'shuriken': shuriken
        }))

    # async def test(self):
    #     self.send(text_data="test response")

    # async def testws(self, input):
    #     self.send(text_data = input)

    # Saving to Redis
    @sync_to_async
    def save_game(self, game_name):
        Game.objects.create(name=game_name, startDate=datetime.datetime.now())

    @sync_to_async
    def save_player(self, player):
        Player.objects.create(
            username=player['username'], 
            posX=player['posX'], 
            posY=player['posY'],
            gameName=self.game_name,
            health=100,
            points=0
        )

    @sync_to_async
    def save_shuriken(self, shuriken):
        Shuriken.objects.create(playerName=shuriken['playerName'], posX=shuriken['posX'], posY=shuriken['posY'])
