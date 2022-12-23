import asyncio
import websockets
import  json
import time

async def send_data(websocket, path):
    while True:

        data = ["{\"message\":\"event-463809::{\\\"event_ID\\\":\\\"463809\\\",\\\"actual_color\\\":\\\"blackFont\\\",\\\"rev_from_col\\\":\\\"greenFont\\\",\\\"previous\\\":\\\"0.3%\\\",\\\"forecast\\\":\\\"0.2%\\\",\\\"actual\\\":\\\"0.2%\\\",\\\"rev_from\\\":\\\"0.2%\\\"}\"}"]
       # data2 =["{\"message\":\"event-463803::{\\\"event_ID\\\":\\\"463803\\\",\\\"actual_color\\\":\\\"greenFont\\\",\\\"rev_from_col\\\":\\\"blackFont\\\",\\\"previous\\\":\\\"0.5%\\\",\\\"forecast\\\":\\\"0.1%\\\",\\\"actual\\\":\\\"0.2%\\\",\\\"rev_from\\\":\\\"\\\"}\"}"]
        await websocket.send(json.dumps(data))
        #await websocket.send(json.dumps(data2))
        time.sleep(2)

start_server = websockets.serve(send_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# data recived

#a["{\"message\":\"event-463809::{\\\"event_ID\\\":\\\"463809\\\",\\\"actual_color\\\":\\\"blackFont\\\",\\\"rev_from_col\\\":\\\"greenFont\\\",\\\"previous\\\":\\\"0.3%\\\",\\\"forecast\\\":\\\"0.2%\\\",\\\"actual\\\":\\\"0.2%\\\",\\\"rev_from\\\":\\\"0.2%\\\"}\"}"]

#a["{\"message\":\"event-463803::{\\\"event_ID\\\":\\\"463803\\\",\\\"actual_color\\\":\\\"greenFont\\\",\\\"rev_from_col\\\":\\\"blackFont\\\",\\\"previous\\\":\\\"0.5%\\\",\\\"forecast\\\":\\\"0.1%\\\",\\\"actual\\\":\\\"0.2%\\\",\\\"rev_from\\\":\\\"\\\"}\"}"]

# heartbeat send
# "{\"_event\":\"heartbeat\",\"data\":\"h\"}"
#heartbeat recived
# a["{\"_event\":\"heartbeat\",\"data\":\"h\"}"]
start_server = websockets.serve(send_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
