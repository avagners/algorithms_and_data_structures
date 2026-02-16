class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2:
            return 0
        elif v1 < v2:
            return -1
        else:
            return 1

    def add(self, value):
        newNode = Node(value)
        node = self.head
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
            return
        ascending = 1 if self.__ascending else -1
        while node:
            compare = self.compare(newNode.value, node.value)
            if compare != ascending:
                break
            node = node.next
        if node is None:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        elif node is self.head:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = node
            newNode.prev = node.prev
            newNode.next.prev = newNode
            newNode.prev.next = newNode

    def find(self, val):
        node = self.head
        ascending = 1 if self.__ascending else -1
        while node:
            compare = self.compare(val, node.value)
            if node.value == val:
                return node
            if compare != ascending:
                break
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            return
        if node is self.tail and node is self.head:
            self.tail = None
            self.head = None
        elif node is self.head:
            self.head = node.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = node.prev
            node.prev.next = None
        elif node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev

    def clean(self, asc):
        self.__ascending = asc
        while self.head:
            self.head = self.head.next
        self.tail = None

    def len(self):
        node = self.head
        result = []
        while node:
            result.append(node)
            node = node.next
        return len(result)

    def get_all(self):
        r = []
        node = self.head
        while node:
            r.append(node)
            node = node.next
        return r

    def print_all_values(self):
        node = self.head
        while node is not None:
            print(node.value, end=' => ')
            node = node.next

    def is_asc(self):
        return self.__ascending


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        return super().compare(v1.split(), v2.split())
