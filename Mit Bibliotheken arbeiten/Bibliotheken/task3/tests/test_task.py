import unittest

from task import create_dataframe


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertIsNotNone(create_dataframe())
