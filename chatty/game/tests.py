from django.test import TestCase

from chatty.game.consumers import GameConsumer

from channels.testing import WebsocketCommunicator
from channels.testing import HttpCommunicator
# from channels.testing import ApplicationCommunicator
class MyTests(TestCase):
    async def test_my_consumer(self):
        communicator = HttpCommunicator(GameConsumer, "GET", "/test/")
        response = await communicator.get_response()
        self.assertEqual(response["body"], b"test response")
        self.assertEqual(response["status"], 200)

    async def test_WebsocketCommunicator(self):
        communicator = WebsocketCommunicator(GameConsumer.as_asgi(), "/testws/")
        connected, subprotocol = await communicator.connect()
        assert connected
        # Test sending text
        await communicator.send_to(text_data="hello")
        response = await communicator.receive_from()
        assert response == "hello"
        # Close
        await communicator.disconnect()
