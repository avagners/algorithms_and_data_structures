class PowerSet:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def put(self, value):
        if value in self.items:
            return
        self.items.append(value)

    def get(self, value):
        if value in self.items:
            return True
        return False

    def remove(self, value):
        if self.get(value):
            self.items.remove(value)
            return True
        return False

    def intersection(self, set2):
        small_set = self if self.size() <= set2.size() else set2
        big_set = self if self.size() >= set2.size() else set2
        result_set = PowerSet()
        for item in small_set.items:
            if item in big_set.items:
                result_set.put(item)
        return result_set

    def union(self, set2):
        small_set = self if self.size() <= set2.size() else set2
        big_set = self if self.size() >= set2.size() else set2
        result = PowerSet()
        result.items = big_set.items.copy()
        for item in small_set.items:
            result.put(item)
        return result

    def difference(self, set2):
        result = PowerSet()
        result.items = self.items.copy()
        for item in set2.items:
            result.remove(item)
        return result

    def issubset(self, set2):
        for item in set2.items:
            if item not in self.items:
                return False
        return True
