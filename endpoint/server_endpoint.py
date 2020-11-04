from aiohttp import web
import asyncio
import random
import socket
import threading


class TCPserver:
    def __init__(self,ip):
        self.ip = ip
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.sock.bind((self.ip,5080))
        self.sock.listen(10)
        while True:
            self.conn, self.addr = self.sock.accept()
            print("SERVER STARTED")
            print(self.conn, self.addr)
    
    def snd_data(self):
        self.sock.send(("Asdsa"))

TCPserver("127.0.0.1")

# async def handle(request):
#     await asyncio.sleep(random.randint(0, 1))
#     #get_data = request.rel_url.query['user']
#     post_data = await request.post()
#     # app = post_data['app']
#     # time_data = post_data['time']
#     # date = post_data['date']
#     description = post_data['description']
   

#     save_file = open("connection_rcv.logs", "a")
#     save_file.write(str(description)+str("\n"))
#     save_file.close()

#     print(description)
#     #print(get_data)
#     return web.Response(text="Thread Started")

# async def init():
#     app = web.Application()
#     app.router.add_route('POST', '/add_client', handle)
#     return await loop.create_server(
#         app.make_handler(), '127.0.0.1', 5091)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(init()))
# loop.run_forever()