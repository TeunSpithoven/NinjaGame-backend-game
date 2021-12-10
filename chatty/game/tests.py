from django.test import TestCase
from channels.testing import HttpCommunicator
from channels.testing import WebsocketCommunicator
from game.consumers import GameConsumer

class MyTests(TestCase):
    async def test_my_consumer(self):
        communicator = WebsocketCommunicator(GameConsumer.as_asgi(), "/ws/test")
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        await communicator.send_to(text_data="hello")
        response = await communicator.receive_from()
        assert response == "hello"
        # Close
        await communicator.disconnect()