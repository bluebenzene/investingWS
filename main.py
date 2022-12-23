import time
import json
import ssl
import threading
from websocket import create_connection
import re


def heartbeat():
    while True:
        ws.send("{\"_event\":\"heartbeat\",\"data\":\"h\"}")
        print("Heartbeat sent")
        time.sleep(3)


data1 = r"event-463803::{\\\"actual\\\":\\\"(\d+\.\d+)%\\\""
data2 = r"event-463809::{\\\"actual\\\":\\\"(\d+\.\d+)%\\\""


def consumer():
    while True:
        # message = ws.recv()
        # match1 = re.search(data1, message)
        # match2 = re.search(data2,message)
        print(ws.recv())




headers = json.dumps({
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en,en-US;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
    "Host": "streaming.forexpros.com",
    "Origin": "https://www.investing.com",
    "Pragma": "no-cache",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
    "Sec-WebSocket-Key": "nM7xi+bAGVUvmzzljPB2rg==",
    "Sec-WebSocket-Version": "13",
    "Upgrade": "websocket",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36 "
})

ws = create_connection('wss://streaming.forexpros.com/echo/087/ep8fkebv/websocket', headers=headers,
                       sslopt={"cert_reqs": ssl.CERT_NONE})

ws.send(
    "{\"_event\":\"bulk-subscribe\",\"tzID\":8,"
    "\"message\":\"event-463809:%%event-463803:\"}"
)
c = threading.Thread(name='consumer', target=consumer)
h = threading.Thread(name='heartbeat', target=heartbeat)

h.start()
c.start()

# import asyncio
# import websockets
# import json
#
#
# async def consumer_handler(websocket):
#     async for message in websocket:
#         print(f"Received message: {message}")
#
#
# async def ping(websocket):
#     while True:
#         await websocket.ping("{\"_event\":\"heartbeat\",\"data\":\"h\"}")
#         await asyncio.sleep(30)
#
#
# async def submessage(websocket):
#     await  websocket.send(
#         "{\"_event\":\"bulk-subscribe\",\"tzID\":8,"
#         "\"message\":\"pid-1175152:%%pid-1175153:%%pid-169:%%pid-166:%%pid-14958:%%pid-44336:%%pid-8827:%%event-463724"
#         ":%%event-463725:%%event-463726:%%event-463727:%%event-464525:%%event-463745:%%event-463749:%%event-463750:%%event"
#         "-463776:%%event-463777:%%event-464559:%%event-463794:%%event-463791:%%event-463672:%%event-463803:%%event-463809"
#         ":%%event-463810:%%event-463800:%%event-463802:%%event-463801:%%event-463807:%%event-463808:%%event-463804:%%event"
#         "-463805:%%event-463806:%%event-463799:%%event-464511:%%event-463824:%%event-463817:%%event-463816:%%event-463814"
#         ":%%event-463815:%%event-463813:%%event-463812:%%event-463818:%%event-463821:%%event-463822:%%event-464483:%%event"
#         "-464484:%%event-464493:%%event-464497:%%event-464498:%%event-464505:%%event-464501:%%event-464499:%%event-464491"
#         ":%%event-464503:%%event-464489:%%event-464500:%%event-464506:%%event-464504:%%event-464495:%%event-464487:%%event"
#         "-464486:%%event-464492:%%event-464485:%%event-464494:%%event-464488:%%event-464496:%%isOpenExch-1:%%isOpenExch-2"
#         ":%%isOpenPair-1175152:%%isOpenPair-1175153:%%isOpenPair-44336:%%isOpenPair-8827:%%domain-1:\"} "
#
#     )
#
#
# # async def heartbeat(websocket):
# #     while True:
# #         await websocket.send("{\"_event\":\"heartbeat\",\"data\":\"h\"}")
# #         await asyncio.sleep(3)
#
#
# headers = json.dumps({
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en,en-US;q=0.9",
#     "Cache-Control": "no-cache",
#     "Connection": "Upgrade",
#     "Host": "streaming.forexpros.com",
#     "Origin": "https://www.investing.com",
#     "Pragma": "no-cache",
#     "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
#     "Sec-WebSocket-Key": "nM7xi+bAGVUvmzzljPB2rg==",
#     "Sec-WebSocket-Version": "13",
#     "Upgrade": "websocket",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/108.0.0.0 Safari/537.36 "
# })
#
#
# async def connect():
#     async with websockets.connect("wss://streaming.forexpros.com/echo/087/ep8fkebv/websocket"
#                                   ) as websocket:
#         submessage_task = asyncio.ensure_future(submessage(websocket))
#         consumer_task = asyncio.ensure_future(consumer_handler(websocket))
#         # heartbeat_task = asyncio.ensure_future(heartbeat(websocket))
#         ping_task = asyncio.ensure_future(ping(websocket))
#
#         await asyncio.gather(submessage_task, consumer_task, ping_task)
#
#
# asyncio.get_event_loop().run_until_complete(connect())
#
# event-463803-actual
#
# event-463809-actual

# "{\"message\":\"event-463803::{\\\"actual\\\":\\\"0.1%\\\",\"}"
# "{\"message\":\"event-463809::{\\\"actual\\\":\\\"0.1%\\\",\"}"
