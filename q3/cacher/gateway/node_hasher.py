import bisect
from hashlib import md5


class Hasher:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.hash = lambda key: int(
            md5(str(key).encode('utf-8')).hexdigest(), 16)
        hash_tuples = [self.hash(j) for j in self.nodes]
        hash_tuples.sort()
        self.hash_tuples = hash_tuples

    def get_node(self, key):
        key_hash = self.hash(key)
        if key_hash > self.hash_tuples[-1]:
            return self.hash_tuples[0]
        index = bisect.bisect_left(self.hash_tuples, key_hash)
        return self.hash_tuples[index]
