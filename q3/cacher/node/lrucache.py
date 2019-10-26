from collections import OrderedDict
from datetime import datetime, timedelta
from .cache_threads import CleanCache
from .storage import Memory
from .sizedcache import SizedCache
from copy import deepcopy
from threading import RLock
from .locker import lock_operation


class LRUCache(SizedCache):
    def __init__(self, duration=2, can_expire=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.duration = duration
        self.exp_times = OrderedDict()
        self.can_expire = can_expire
        self.lock = RLock()
        self.related = [self.exp_times]
        if can_expire:
            cleaner = CleanCache(self, clear_time=duration)
            cleaner.start()

    @lock_operation
    def get(self, key):
        value = super().get(key)
        self._set_expiration_time(key)
        return value

    def delete_expired(self):
        check_time = datetime.now()
        if self.can_expire and self.duration:
            exp_times = deepcopy(self.exp_times)
            for key in exp_times:
                if exp_times[key] < check_time:
                    self.delete(key)

    @lock_operation
    def _set_expiration_time(self, key):
        self.exp_times.pop(key, None)
        self.exp_times[key] = datetime.now() + timedelta(seconds=self.duration)

    @lock_operation
    def set(self, key, value):
        super().set(key, value)
        self._set_expiration_time(key)

    @lock_operation
    def delete(self, key):
        super().delete(key)
        self.exp_times.pop(key, None)
