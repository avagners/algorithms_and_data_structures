import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from stack.Stack import Stack


class QueueStack:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.size() > 0:
            return self.out_stack.pop()
        while self.in_stack.size() > 0:
            item = self.in_stack.pop()
            self.out_stack.push(item)
        return self.out_stack.pop()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()
