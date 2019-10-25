from cacher.lrucache import LRUCache


if __name__ == "__main__":
    x = LRUCache(duration=30, max_size=3, can_expire=False)
    x['id'] = 10
    x['23'] = 10
    x['we'] = 10
    x['wed'] = 10

    cache = LRUCache(duration=8, max_size=3, can_expire=True)
    cache['peter'] = 10
    cache['id'] = 10
    cache['23'] = 10
    cache['we'] = 10
    cache['wed'] = 10
