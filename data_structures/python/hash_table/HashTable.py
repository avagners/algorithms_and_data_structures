class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash = sum([ord(sym) for sym in value]) % self.size
        return hash

    def seek_slot(self, value):
        index = self.hash_fun(value)
        count = 0
        while count < self.size:
            if self.slots[index] is None:
                return index
            index += self.step
            if index >= self.size:
                index %= self.size
            count += 1
        return None

    def put(self, value):
        index = self.seek_slot(value)
        if type(index) is int:
            self.slots[index] = value
        return index

    def find(self, value):
        index = self.hash_fun(value)
        count = 0
        while count < self.size:
            if self.slots[index] == value:
                return index
            index += self.step
            if index >= self.size:
                index %= self.size
            count += 1
        return None
