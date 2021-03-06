from core.UserAgent import get_user_agent
from core.DictCreate import DictCreate
from core.Asynchronous import Asynchronous
from core.Requester import Requester


class Controller:
    def __init__(self, options):
        self.progress = 0
        self.options = options
        self.headers = {
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
        }
        # Set Headers
        if self.options.cookie:
            self.setHeaders("Cookie", self.options.cookie)
        self.setHeaders("User-Agent", get_user_agent())
        # Create Dict
        self.List = DictCreate(options).get_content()
        self.list_iter = iter(self.List)
        # Input verification
        if not self.options.url.endswith("/"):
            self.options.url += "/"
        # list size
        print(": "+str(len(self.List)))
        # Start request
        self.pattern()

    # set http's Headers
    def setHeaders(self, key, value):
        self.headers[key.strip()] = value

    # choose mode
    def pattern(self):
        if self.options.asy:
            Asynchronous(self)
        else:
            Requester(self)
