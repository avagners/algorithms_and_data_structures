import random
import unittest

from StackHead import StackHead


class TestStackHeadOneItem(unittest.TestCase):

    def setUp(self):
        self.s_stack = StackHead()
        self.number = random.randint(0, 100)
        self.s_stack.push(self.number)

    def test_one_item_size(self):
        self.assertEqual(self.s_stack.size(), 1)

    def test_one_item_push(self):
        len_stack = self.s_stack.size()
        new_item = random.randint(0, 100)
        self.s_stack.push(new_item)
        self.assertEqual(self.s_stack.size(), len_stack + 1)
        self.assertEqual(self.s_stack.stack[0], new_item)

    def test_one_item_pop(self):
        len_stack = self.s_stack.size()
        pop_result = self.s_stack.pop()
        self.assertEqual(pop_result, self.number)
        self.assertEqual(self.s_stack.size(), len_stack - 1)
        self.assertEqual(self.s_stack.stack, [])

    def test_one_item_peek(self):
        len_stack = self.s_stack.size()
        peek_result = self.s_stack.peek()
        self.assertEqual(peek_result, self.s_stack.stack[0])
        self.assertEqual(self.s_stack.size(), len_stack)
        self.assertEqual(self.s_stack.stack, [self.number])


class TestStackHeadEmpty(unittest.TestCase):

    def setUp(self):
        self.s_stack = StackHead()

    def test_empty_size(self):
        self.assertEqual(self.s_stack.size(), 0)

    def test_empty_push(self):
        len_stack = self.s_stack.size()
        new_item = random.randint(0, 100)
        self.s_stack.push(new_item)
        self.assertEqual(self.s_stack.size(), len_stack + 1)
        self.assertEqual(self.s_stack.stack[0], new_item)

    def test_empty_pop(self):
        len_stack = self.s_stack.size()
        pop_result = self.s_stack.pop()
        self.assertIsNone(pop_result)
        self.assertEqual(self.s_stack.size(), len_stack)
        self.assertEqual(self.s_stack.stack, [])

    def test_empty_peek(self):
        len_stack = self.s_stack.size()
        peek_result = self.s_stack.peek()
        self.assertIsNone(peek_result)
        self.assertEqual(self.s_stack.size(), len_stack)
        self.assertEqual(self.s_stack.stack, [])


class TestStackHeadManyItems(unittest.TestCase):

    def setUp(self):
        self.s_stack = StackHead()
        number = random.randrange(3, 100)
        self.items_list = [random.randint(0, 100) for _ in range(number)]
        for item in self.items_list:
            self.s_stack.push(item)

    def test_many_items_size(self):
        self.assertEqual(self.s_stack.size(), len(self.items_list))

    def test_many_items_push(self):
        new_item = random.randint(101, 1000)
        self.s_stack.push(new_item)
        self.assertEqual(self.s_stack.size(), len(self.items_list) + 1)
        self.assertEqual(self.s_stack.stack[0], new_item)

    def test_many_items_pop(self):
        self.items_list.reverse()
        pop_result = self.s_stack.pop()
        self.assertEqual(pop_result, self.items_list[0])
        self.assertEqual(self.s_stack.size(), len(self.items_list) - 1)
        self.assertListEqual(self.s_stack.stack, self.items_list[1:])

    def test_many_items_peek(self):
        self.items_list.reverse()
        peek_result = self.s_stack.peek()
        self.assertEqual(peek_result, self.items_list[0])
        self.assertEqual(self.s_stack.size(), len(self.items_list))
        self.assertListEqual(self.s_stack.stack, self.items_list)


if __name__ == '__main__':
    unittest.main()
