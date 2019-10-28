from .storage import Memory


class SizedCache():
    related = []

    def __init__(self, max_size=1024):
        self.max_size = max_size
        self.cache = Memory()

    def get(self, key):
        return self.cache[key]

    def set(self, key, value):
        try:
            del self.cache[key]
        except KeyError:
            if len(self.cache) >= self.max_size:
                self.cache.store.popitem(last=False)
                self.__clear_related()
        self.cache[key] = value

    def delete(self, key):
        del self.cache[key]

    def __getitem__(self, key): return self.get(key)

    def __setitem__(self, key, value): return self.set(key, value)

    def __clear_related(self):
        """Clears the last item in objects related to the cache store
        """
        for item in self.related:
            item.popitem(last=False)
