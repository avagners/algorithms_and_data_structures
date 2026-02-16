import unittest

from BloomFilter import BloomFilter

str_dict = {
    'str1': "0123456789",
    'str2': "1234567890",
    'str3': "2345678901",
    'str4': "3456789012",
    'str5': "4567890123",
    'str6': "5678901234",
    'str7': "6789012345",
    'str8': "7890123456",
    'str9': "8901234567",
    'str10': "9012345678",
}


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.m = 32
        self.s_bloom = BloomFilter(self.m)

    def test_empty_filter(self):
        for key in str_dict.keys():
            self.assertFalse(self.s_bloom.is_value(str_dict[key]))

    def test_full_filter(self):
        for key in str_dict.keys():
            self.s_bloom.add(str_dict[key])
        for key in str_dict.keys():
            self.assertTrue(self.s_bloom.is_value(str_dict[key]))


if __name__ == '__main__':
    unittest.main()
