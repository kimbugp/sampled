from collections import OrderedDict
from .exceptions import KeyNotFound


class Memory(object):
    def __init__(self):
        self.store = OrderedDict()

    def __setitem__(self, key, value):
        self.store.pop(key, None)
        self.store[key] = value

    def __getitem__(self, key):
        value = self.store.pop(key, None)
        if value:
            self.store[key] = value
            return value
        raise KeyNotFound("%s not found in cache" % (key))

    def __delitem__(self, key):
        self.store.pop(key)

    def __len__(self):
        return len(self.store)
