import unittest

from task import load_names, filter_long_names


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        names = load_names("names.csv")
        long_names = filter_long_names(names)
        self.assertEqual(len(long_names), 4, msg="Vier Namen sind zu lang.")
