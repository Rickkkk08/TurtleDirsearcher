import sys
# Judge system version
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, we need Python 3.x\n")
    sys.exit(1)
from core.Parser import Parser
from core.Controller import Controller
from core.Printer import Printer


class Program:
    def __init__(self):
        # Receiving parameters
        self.options = Parser().options
        # Output page
        self.out = Printer(self.options)
        # start
        self.controller = Controller(self.options)
        # end
        Printer.end(self.options)


if __name__ == '__main__':
    main = Program()
