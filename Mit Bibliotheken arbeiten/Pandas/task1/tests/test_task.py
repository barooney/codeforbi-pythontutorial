import unittest
import pandas as pd

from task import load_names


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertTrue(isinstance(load_names("names.csv"), pd.DataFrame), msg="load_names gibt einen DataFrame zurück")
