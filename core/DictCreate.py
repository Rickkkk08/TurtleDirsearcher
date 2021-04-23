import linecache
import os
import re


class DictCreate:
    def __init__(self, options):
        if options.dict is None:
            self.path = os.path.split(os.path.realpath(__file__))[0] + '\\..' + '\\db\\' + '\\dict.txt'
        else:
            self.path = "db" + "//" + options.dict

    def get_content(self):
        if os.path.exists(self.path):
            content = []
            cache_data = linecache.getlines(self.path)
            for line in range(len(cache_data)):
                content.append(cache_data[line])
            return content
        else:
            print('the path [{}] is not exist!'.format(self.path))
