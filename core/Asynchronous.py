import aiohttp
import asyncio


class Asynchronous:
    def __init__(self, Controller):
        self.List = Controller.List
        loop = asyncio.get_event_loop()
        tasks = [self.async_get_url(Controller, ex) for ex in self.List]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    async def async_get_url(self, Controller, ex):
        headers = Controller.headers
        async with aiohttp.ClientSession() as session:
            async with session.get(Controller.options.url + ex, headers=headers) as r:
                print(f"{r.status} - {ex}")
