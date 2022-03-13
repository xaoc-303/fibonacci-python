import unittest
from fibo import f1, f2

class TestFiboMethods(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(f1(8), 21)

    def test_f2(self):
        self.assertEqual(f2(8), 21)

if __name__ == '__main__':
    unittest.main()
