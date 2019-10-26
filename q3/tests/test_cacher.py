import unittest

from cacher.node.lrucache import LRUCache


class TestCacheCRUD(unittest.TestCase):
    def test_equal_versions(self):
        cache = LRUCache(3)
        cache['peter'] = 10
        cache['23'] = 10
        cache['we'] = 10
        cache['wed'] = 10
        with self.assertRaises(KeyError):
            x = cache['id']


if __name__ == "__main__":
    unittest.main()
