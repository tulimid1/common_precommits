import unittest


class test_test(unittest.TestCase):
    """test test"""

    def test_1(self):
        """example test"""
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
