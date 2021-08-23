from optparse import OptionParser


class Parser:
    def __init__(self):
        optParser = OptionParser()
        optParser.add_option('-u', '--url', help='Target url', action='store', type="string", dest='url')
        optParser.add_option('-d', '--dict', action='store', type="string", dest='dict')
        optParser.add_option('-c', '--cookie', action='store', type="string", dest='cookie')
        optParser.add_option('-a', '--async', action='store', type="string", dest='asy')
        # optParser.add_option('-e', '--extensions', action='store', type="string", dest="extensions")
        self.options, self.args = optParser.parse_args()
