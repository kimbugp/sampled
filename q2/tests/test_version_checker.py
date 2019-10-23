import unittest

from versioncheck.version_checker import version_checker


class TestVersion(unittest.TestCase):
    def test_equal_versions(self):
        res = version_checker("12.4", "12.4")
        assert res == "12.4 is equal to 12.4"

    def test_first_version_less_than(self):
        res = version_checker("12.1", "12.4")
        assert res == "12.1 is less than 12.4"

    def test_first_version_greater_than(self):
        res = version_checker("12.10", "12.4")
        assert res == "12.10 is greater than 12.4"

    def test_second_version_less_than(self):
        res = version_checker("11.1", "12.4")
        assert res == "11.1 is less than 12.4"

    def test_second_version_greater_than(self):
        res = version_checker("12.10", "12.4")
        assert res == "12.10 is greater than 12.4"

    def test_unequal_version_length_less_than(self):
        res = version_checker("11.1.1", "12.4")
        assert res == "11.1.1 is less than 12.4"

    def test_unequal_version_length_greater_than(self):
        res = version_checker("12.4.2", "12.4")
        assert res == "12.4.2 is greater than 12.4"


if __name__ == "__main__":
    unittest.main()
