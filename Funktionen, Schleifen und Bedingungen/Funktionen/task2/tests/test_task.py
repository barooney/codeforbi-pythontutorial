import unittest

from task import greeting


class TestCase(unittest.TestCase):

    def test_not_forgot_return(self):
        self.assertNotEqual(None, greeting("test"))

    def test_not_only_name(self):
        self.assertNotEqual("test", greeting("test"))
        self.assertNotEqual("asdf", greeting("asdf"))

    def test_contains_name(self):
        self.assertTrue("test" in greeting("test"))
        self.assertTrue("asdf" in greeting("asdf"))
