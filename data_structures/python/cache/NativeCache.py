class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        hash = sum([ord(sym) for sym in key]) % self.size
        return hash

    def is_key(self, key):
        return key in self.slots

    def get_hit(self, key):
        if not self.is_key(key):
            return None
        index = self.hash_fun(key)
        count = 0
        while count < self.size:
            if self.slots[index] == key:
                return self.hits[index]
            index += 1
            if index >= self.size:
                index %= self.size
            count += 1

    def get_value(self, key):
        if not self.is_key(key):
            return None
        index = self.hash_fun(key)
        count = 0
        while count < self.size:
            if self.slots[index] == key:
                self.hits[index] += 1
                return self.values[index]
            index += 1
            if index >= self.size:
                index %= self.size
            count += 1

    def is_full(self):
        return None not in self.slots

    def put(self, key, value):
        index = self.hash_fun(key)
        count = 0
        while count < self.size:
            if self.is_key(key) and self.slots[index] == key:
                self.values[index] = value
                break
            if not self.is_key(key) and self.is_full():
                min_hit = min(self.hits)
                index = self.hits.index(min_hit)
                self.slots[index] = key
                self.values[index] = value
                self.hits[index] = 0
                break
            if not self.is_key(key) and self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                break
            index += 1
            if index >= self.size:
                index %= self.size
            count += 1
