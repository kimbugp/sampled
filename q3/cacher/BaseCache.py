from collections import OrderedDict
from .exceptions import KeyNotFound


class BaseCache():
    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.cache = OrderedDict()

    def __getitem__(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
        except KeyNotFound:
            raise KeyNotFound("%s not found in cache" % (key))
        return value

    def __setitem__(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
        self.cache[key] = value

    def __delete__(self, key):
        if key in self.cache.keys():
            del self.cache[key]
        raise KeyNotFound("%s not found in cache" % (key))
