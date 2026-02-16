class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        hash = sum([ord(sym) for sym in key]) % self.size
        return hash

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        count = 0
        while count < self.size:
            if self.is_key(key) and self.slots[index] == key:
                self.values[index] = value
                return
            if not self.is_key(key) and self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                return
            index += 1
            if index >= self.size:
                index %= self.size
            count += 1

    def get(self, key):
        if not self.is_key(key):
            return None
        index = self.hash_fun(key)
        count = 0
        while count < self.size:
            if self.slots[index] == key:
                return self.values[index]
            index += 1
            if index >= self.size:
                index %= self.size
            count += 1
