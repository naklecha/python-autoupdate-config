import websockets
import json
import asyncio

data = {}

async def listen(uri):
    async with websockets.connect(uri) as websocket:
        key = input("Key: ")
        value = input("Value: ")
        await websocket.send(json.dumps({"operation":"update", "key":key, "value":value}))
        data = json.loads(await websocket.recv())
        print(data)

if(__name__ == "__main__"):
    asyncio.get_event_loop().run_until_complete(listen(uri = "ws://localhost:5000"))
