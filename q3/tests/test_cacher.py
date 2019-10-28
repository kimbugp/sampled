import unittest

from cacher.node.lrucache import LRUCache


class TestCacheCRUD(unittest.TestCase):
    def test_get_key_when_cache_is_full_raise_key_error(self):
        cache = LRUCache(3, max_size=3)
        cache['score'] = 10
        cache['age'] = 10
        cache['max'] = 10
        cache['wed'] = 10
        with self.assertRaises(KeyError):
            x = cache['score']

    def test_get_key_when_cache_is_not_full_returns(self):
        cache = LRUCache(3)
        cache['score'] = 10
        cache['age'] = 10
        cache['max'] = 10
        x = cache['score']
        self.assertEqual(x, 10)

    def test_last_key_is_removed_when_cache_is_full(self):
        cache = LRUCache(3, max_size=2)
        cache['score'] = 10
        cache['age'] = 10
        cache['max'] = 10
        with self.assertRaises(KeyError):
            x = cache['score']


if __name__ == "__main__":
    unittest.main()
