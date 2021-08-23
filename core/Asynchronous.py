import aiohttp
import asyncio
from core.Printer import Printer


async def async_get_url(Controller, ex):
    try:
        headers = Controller.headers
        async with aiohttp.ClientSession() as session:
            async with session.get(Controller.options.url + ex, headers=headers) as r:
                print(f"[*]   {r.url} {r.status}")
    except KeyboardInterrupt:
        print("\nUser Interrupt")
        exit(0)


class Asynchronous:
    def __init__(self, Controller):
        print("Async Mode")
        self.List = Controller.List
        loop = asyncio.get_event_loop()
        tasks = [async_get_url(Controller, ex) for ex in self.List]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
        self.progress = 0
