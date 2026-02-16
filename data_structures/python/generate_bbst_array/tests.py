import unittest

from generate_bbst_array import GenerateBBSTArray


class TestGenerateBBSTArray(unittest.TestCase):

    def test_empty_array(self):
        a = []
        self.assertFalse(GenerateBBSTArray(a))
        self.assertIsInstance(GenerateBBSTArray(a), list)
        self.assertEqual(GenerateBBSTArray(a), [])

    def test_one_level(self):
        a = [1]
        self.assertTrue(GenerateBBSTArray(a))
        self.assertIsInstance(GenerateBBSTArray(a), list)
        self.assertEqual(GenerateBBSTArray(a), [1])

    def test_two_levels(self):
        a = [1, 2, 3]
        self.assertTrue(GenerateBBSTArray(a))
        self.assertIsInstance(GenerateBBSTArray(a), list)
        self.assertEqual(GenerateBBSTArray(a), [2, 1, 3])

    def test_three_levels(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        self.assertTrue(GenerateBBSTArray(a))
        self.assertIsInstance(GenerateBBSTArray(a), list)
        self.assertEqual(GenerateBBSTArray(a), [4, 2, 6, 1, 3, 5, 7])

    def test_four_levels(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertTrue(GenerateBBSTArray(a))
        self.assertIsInstance(GenerateBBSTArray(a), list)
        self.assertEqual(
            GenerateBBSTArray(a),
            [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        )


if __name__ == '__main__':
    unittest.main()
