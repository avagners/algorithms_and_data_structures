class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        # 17
        hash = 0
        for c in str1:
            code = ord(c)
            hash = (hash * 17 + code) % self.filter_len
        return 1 << hash

    def hash2(self, str1):
        # 223
        hash = 0
        for c in str1:
            code = ord(c)
            hash = (hash * 223 + code) % self.filter_len
        return 1 << hash

    def add(self, str1):
        self.filter |= (self.hash1(str1) | self.hash2(str1))

    def is_value(self, str1):
        hash1 = self.filter & self.hash1(str1)
        hash2 = self.filter & self.hash2(str1)
        return hash1 > 0 and hash2 > 0
