import unittest

from task import kommentar


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_kombinationen(self):
        komm1 = kommentar(1).replace(str(1), "")
        komm2 = kommentar(2).replace(str(2), "")
        komm3 = kommentar(3).replace(str(3), "")
        komm4 = kommentar(4).replace(str(4), "")
        komm5 = kommentar(5).replace(str(5), "")
        komm6 = kommentar(6).replace(str(6), "")

        self.assertNotEqual(komm1, "Ein guter Anfang")

        self.assertEqual(komm1, komm2)
        self.assertEqual(komm3, komm4)
        self.assertNotEqual(komm1, komm3)
        self.assertNotEqual(komm1, komm4)
        self.assertNotEqual(komm2, komm3)
        self.assertNotEqual(komm2, komm4)

        self.assertNotEqual(komm1, komm5)
        self.assertNotEqual(komm1, komm6)
        self.assertNotEqual(komm3, komm5)
        self.assertNotEqual(komm4, komm6)
        self.assertNotEqual(komm5, komm6)
