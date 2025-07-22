import unittest
from scitani import scitani

class TestScitani(unittest.TestCase):
    def test_spravne(self):
        self.assertEqual(scitani(2, 3), 5)
        self.assertEqual(scitani(2.51, 3.51), 6.02)
        self.assertEqual(scitani(-1, 3), 2)

    def test_chyba_typ(self):
        with self.assertRaises(TypeError):
            scitani("jarda", 158)
        with self.assertRaises(TypeError):
            scitani(11, None)
        with self.assertRaises(TypeError):
            scitani([1], 2)

if __name__ == '__main__':
    unittest.main()