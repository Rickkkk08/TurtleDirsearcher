import time
import datetime
from thirdparty import requests
from core.UserAgent import get_user_agent
from core.DictCreate import DictCreate
from core.Printer import Printer
from core.Asynchronous import Asynchronous


class Controller:
    def __init__(self, options):
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
        # Start request
        self.pattern()

    # set http's Headers
    def setHeaders(self, key, value):
        self.headers[key.strip()] = value

    def requester(self):
        while True:
            try:
                # Clear carriage return
                ex = (next(self.list_iter)).strip()
                # Making requests
                r = requests.get(self.options.url + ex, headers=self.headers, verify=False)
                '''
                # Output progress
                percent = str(int(round(self.progress) / round(len(self.list)) * 100))
                print(percent + "%   " + ex.ljust(110) + "\r", end='')
                '''
                # Output result
                Printer.printLine(r)
            except StopIteration:
                break

    def pattern(self):
        if self.options.asy == "1":
            print("async mode start")
            Asynchronous(self)
        else:
            print("normal mode start")
            self.requester()
