import sys
sys.path.insert(0, '/home/jovyan/knowknow')
from knowknow import *

from os.path import expanduser
home = expanduser("~")

def genlim(limit):
    def limiter(gen):
        for i,item in enumerate(gen):
            if i > limit:
                break
            yield item
    return limiter

class categorical:
    def __init__(self):
        self.items = []
    def __getitem__(self, x):
        if type(x) == int:
            return self.items[x]
        
        if x in self.items:
            return self.items.index(x)
        
        self.items.append(x)
        return len(self.items) - 1