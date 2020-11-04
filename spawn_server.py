from asyncio_http import *

for port in range(8003,8034):
    try: 
        loop.run_until_complete(asyncio.gather(init(port)))
    except Exception as error: 
        print(error)
        pass
loop.run_forever()