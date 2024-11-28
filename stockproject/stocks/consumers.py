from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class StocksConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self, *args, **kwargs):
        print("Received connection req")
        await self.channel_layer.group_add('stocks', self.channel_name)
        await self.accept()
        print("Connection Accepted")

    async def disconnect(self, *args, **kwargs):
        await self.channel_layer.group_discard('stocks', self.channel_name)

    async def send_stock_details(self, event):
        stock_details_message=json.loads(event['stock-details'])

        await self.send(json.dumps(stock_details_message))
