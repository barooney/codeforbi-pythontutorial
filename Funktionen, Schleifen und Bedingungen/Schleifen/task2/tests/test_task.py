import unittest

from task import training


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(training(10, 10), 100)
        self.assertEqual(training(10, 20), 200)
        self.assertEqual(training(20, 20), 400)
        self.assertEqual(training(0, 100), 0)
        self.assertEqual(training(100, 0), 0)
