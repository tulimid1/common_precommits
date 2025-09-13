import unittest


class test_test(unittest.TestCase):
    """test test"""

    def test_1(self):
        """example test"""
        self.assertEqual(1 + 1, 2)

    def test_2(self):
        """example test"""
        self.assertEqual(1 + 3, 4)


if __name__ == "__main__":
    unittest.main()
