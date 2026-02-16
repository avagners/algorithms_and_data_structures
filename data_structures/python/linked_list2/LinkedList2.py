class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        result = []
        while node:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node:
            if node.value == val:
                if node is self.tail and node is self.head:
                    self.tail = None
                    self.head = None
                elif node is self.tail:
                    self.tail = node.prev
                    node.prev.next = None
                elif node.prev:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    if not all:
                        break
                else:
                    self.head = node.next
                    self.head.prev = None
                    if not all:
                        break
            node = node.next

    def insert(self, afterNode, newNode):
        node = self.head
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
            return
        while node:
            if node == afterNode:
                break
            node = node.next
        if node is None:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            newNode.next = node.next
            newNode.prev = node
            node.next = newNode
            if node is self.tail:
                self.tail = newNode

    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode

    def clean(self):
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
