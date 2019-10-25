from threading import Thread, RLock
import time
import weakref
import logging


class CleanCache(Thread):
    def __init__(self, cache, clear_time=60):
        self.reference = weakref.ref(cache)
        self.clear_time = clear_time
        super().__init__()

    def run(self):
        while self.reference():
            ref = self.reference()
            if ref:
                expired_items = ref.delete_expired()
                time.sleep(self.clear_time)
            ref = None
