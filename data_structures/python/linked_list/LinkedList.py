class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val, all=False):
        node = self.head
        previous = None
        while node:
            if node.value == val:
                if node is self.tail:
                    self.tail = previous
                if previous:
                    previous.next = node.next
                    if not all:
                        break
                else:
                    self.head = node.next
                    if not all:
                        break
            else:
                previous = node
            node = node.next

    def clean(self):
        while self.head:
            self.head = self.head.next
        self.tail = None

    def find_all(self, val):
        node = self.head
        result = []
        while node:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def len(self):
        node = self.head
        result = []
        while node:
            result.append(node)
            node = node.next
        return len(result)

    def insert(self, afterNode, newNode):
        node = self.head
        while node:
            if node == afterNode:
                break
            node = node.next
        if node is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            newNode.next = node.next
            node.next = newNode
            if node is self.tail:
                self.tail = newNode
