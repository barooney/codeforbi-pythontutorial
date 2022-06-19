import unittest

from task import load_names


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        df = load_names("names.csv")
        self.assertEqual(df.at[3, "firstname"], "Simon", msg="Der Name wurde von Simeon zu Simon geändert.")
        self.assertFalse(17 in df, msg="Asif Ramos wurde aus der Liste entfernt.")
        self.assertEqual(df["fullname"][0], "Kiya Leblanc", msg="Die Spalte fullname wird korrekt gebildet.")
        self.assertEqual(df["length"][0], 12, msg="Die Länge des vollen Namens wird korrekt berechnet.")
