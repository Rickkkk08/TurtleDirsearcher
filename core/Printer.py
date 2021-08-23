import datetime
import time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


class NoColor:
    RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = BRIGHT = RESET_ALL = ''


class Printer:
    def __init__(self, options):
        self.name = """
         ____  _  _      ____  _     _____
        / ___\/ \/ \__/|/  __\/ \   /  __/
        |    \| || |\/|||  \/|| |   |  \  
        \___ || || |  |||  __/| |_/\|  /_ 
        \____/\_/\_/  \|\_/   \____/\____\ by rick V1.1
        
                                                        """
        self.banner()
        self.start(options)

    def banner(self):
        print(self.name)

    @staticmethod
    def start(options):
        options.start_time = time.time()
        print("Target URL:" + options.url + "   HTTP Method = GET"+"   Wordlist size", end='')

    @staticmethod
    def end(options):
        options.end_time = time.time()
        timeSpend = round(options.end_time - options.start_time,3)
        print("\n耗时:" + str(timeSpend) +"s")

    @staticmethod
    def printLine(r):
        # status = r.status_code
            dt = datetime.datetime.now().strftime('%H:%M:%S')
            message = "[" + dt + "]" + f"   {r.request.path_url} --> {r.status_code}"
            status = r.status_code
            if status == 200:
                message = Fore.GREEN + message + Style.RESET_ALL

            elif 300 < status < 310:
                message_redirect = "[" + dt + "]" + f"   {r.request.path_url} --> {r.headers['Location']} --{r.status}"
                message_redirect = Fore.CYAN + message + Style.RESET_ALL
                print(message_redirect)

            elif status == 401:
                message = Fore.YELLOW + message + Style.RESET_ALL

            elif status == 403:
                message = Fore.BLUE + message + Style.RESET_ALL

            elif status == 500:
                message = Fore.RED + message + Style.RESET_ALL

            if status == 404 or 300 < status < 301:
                pass
            else:
                print(message)
