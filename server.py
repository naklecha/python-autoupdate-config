import asyncio
import websockets
import json

connected = set()
config = {}

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            message = json.loads(message)
            if(message["operation"] == "update"):
                config[message["key"]] = message["value"]
            if(message["operation"] == "remove"):
                if(message["key"] in config):
                    config.pop(message["key"])

            if(message["operation"] == "get"):
                await websocket.send(json.dumps(config))
            else:
                for conn in connected:
                    await conn.send(json.dumps(config))
    finally:
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
    

