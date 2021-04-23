import datetime
import time
from thirdparty.colorama import init, Fore, Style


class Printer:
    def __init__(self, options):
        self.name = """
         ____  _  _      ____  _     _____
        / ___\/ \/ \__/|/  __\/ \   /  __/
        |    \| || |\/|||  \/|| |   |  \  
        \___ || || |  |||  __/| |_/\|  /_ 
        \____/\_/\_/  \|\_/   \____/\____\ by rick V0.0.1"""
        self.banner()
        self.start(options)

    def banner(self):
        print(self.name)

    @staticmethod
    def start(options):
        options.start_time = time.time()
        print("Target URL:" + options.url)

    @staticmethod
    def end(options):
        options.end_time = time.time()
        timeSpend = options.end_time - options.start_time
        print("耗时:" + str(timeSpend))

    @staticmethod
    def printLine(r):
        # status = r.status_code
        dt = datetime.datetime.now().strftime('%H:%M:%S')
        message = "[" + dt + "]" + f"   {r.request.path_url} --> {r.status_code}"
        print(message)
