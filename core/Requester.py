from core.Printer import Printer
import requests


def req_get_url(Controller):
    print("Normal Mode")
    while True:
        try:
            try:

                # progress update
                Controller.progress = Controller.progress + 1
                # Clear carriage return
                ex = (next(Controller.list_iter)).strip()
                # Making requests
                r = requests.get(Controller.options.url + ex, headers=Controller.headers, verify=False)
                # Output progress
                percent = (str(int(round(Controller.progress) / round(len(Controller.List)) * 100)))
                print(percent + "%   " + ex.ljust(110) + "\r", end='')
                # Output result
                Printer.printLine(r)

            except StopIteration:
                Printer.end(options=Controller.options)
                print("Finish Scanning")
                exit(0)
        except KeyboardInterrupt:
            Printer.end(options=Controller.options)
            print("User Interrupt")
            exit(0)


class Requester:
    def __init__(self, Controller):
        req_get_url(Controller)
