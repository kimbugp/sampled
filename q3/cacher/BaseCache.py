from collections import OrderedDict
from .exceptions import KeyNotFound
from datetime import datetime, timedelta
from .cache_threads import CleanCache


class BaseCache():
    def __init__(self, max_size=1024, duration=2, can_expire=False):
        self.max_size = max_size
        self.cache = OrderedDict()
        self.duration = duration
        self.exp_times = OrderedDict()
        if can_expire:
            cleaner = CleanCache(clear_time=duration)
            cleaner.start()

    def __getitem__(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            self._set_expiration_time(key)
        except KeyNotFound:
            raise KeyNotFound("%s not found in cache" % (key))
        return value

    def delete_expired(self):
        check_time = datetime.now()
        if self.duration:
            for key in self.exp_times:
                if self.exp_times[key] >= check_time:
                    self.__delete__(key)

    def _set_expiration_time(self, key):
        self.exp_times[key] = datetime.now() + timedelta(seconds=self.duration)

    def __setitem__(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
        self.cache[key] = value
        self._set_expiration_time(key)

    def __delete__(self, key):
        if key in self.cache.keys():
            del self.cache[key]
            del self.exp_times[key]
        raise KeyNotFound("%s not found in cache" % (key))
