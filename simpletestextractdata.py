import asyncio
import json

import websockets
import re


async def receive_messages(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        # clean_data = message.replace("\\", "")
        # print(clean_data)
        pattern = r"event-463809::{\\\"actual\\\":\\\"(\d+\.\d+)%"
        match = re.search(pattern, message)
        if match:
            event = match.group(1)
            actual = match.group(2)
            print(f"Event: {event}, Actual: {actual}")
        else:
            print("Data is not present in the message.")


async def connect_to_server():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await receive_messages(websocket, "/")


asyncio.get_event_loop().run_until_complete(connect_to_server())
