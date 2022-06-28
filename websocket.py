import asyncio
import websockets

async def accept(websocket_server):
    while True:
        data = await websocket_server.recv()
        print(f"Received: {data}")
        await websocket_server.send(f"echo: {data}")

start_server = websockets.serve(accept, "localhost", 9998)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()