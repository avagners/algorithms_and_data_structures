import random
import unittest

from Deque import Deque
from check_palidrome import check_palidrome


class TestDequeOneItem(unittest.TestCase):

    def setUp(self):
        self.s_deque = Deque()
        self.number = random.randint(0, 100)
        self.s_deque.addTail(self.number)

    def test_one_item_size(self):
        self.assertEqual(self.s_deque.size(), 1)

    def test_one_item_add_tail(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.addTail(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[-1], new_item)

    def test_one_item_add_front(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.addFront(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[0], new_item)

    def test_one_item_remove_tail(self):
        len_queue = self.s_deque.size()
        result_remove = self.s_deque.removeTail()
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertEqual(result_remove, self.number)
        self.assertListEqual(self.s_deque.deque, [])

    def test_one_item_remove_front(self):
        len_queue = self.s_deque.size()
        result_remove = self.s_deque.removeTail()
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertEqual(result_remove, self.number)
        self.assertListEqual(self.s_deque.deque, [])


class TestDequeEmpty(unittest.TestCase):

    def setUp(self):
        self.s_deque = Deque()

    def test_empty_size(self):
        self.assertEqual(self.s_deque.size(), 0)

    def test_empty_add_tail(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.addTail(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[-1], new_item)

    def test_empty_add_front(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.addFront(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[0], new_item)

    def test_empty_remove_tail(self):
        len_queue = self.s_deque.size()
        result_remove = self.s_deque.removeTail()
        self.assertEqual(self.s_deque.size(), len_queue)
        self.assertIsNone(result_remove)
        self.assertListEqual(self.s_deque.deque, [])

    def test_one_item_remove_front(self):
        len_queue = self.s_deque.size()
        result_remove = self.s_deque.removeTail()
        self.assertEqual(self.s_deque.size(), len_queue)
        self.assertIsNone(result_remove)
        self.assertListEqual(self.s_deque.deque, [])


class TestDequeManyItems(unittest.TestCase):

    def setUp(self):
        self.s_deque = Deque()
        number = random.randrange(3, 100)
        self.items_list = [random.randint(0, 100) for _ in range(number)]
        for item in self.items_list:
            self.s_deque.addTail(item)

    def test_many_items_size(self):
        self.assertEqual(self.s_deque.size(), len(self.items_list))

    def test_many_items_add_tail(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.addTail(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[-1], new_item)

    def test_many_items_add_front(self):
        len_queue = self.s_deque.size()
        new_item = random.randint(0, 100)
        self.s_deque.addFront(new_item)
        self.assertEqual(self.s_deque.size(), len_queue + 1)
        self.assertEqual(self.s_deque.deque[0], new_item)

    def test_many_items_remove_tail(self):
        len_queue = self.s_deque.size()
        result_remove = self.s_deque.removeTail()
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertEqual(result_remove, self.items_list[-1])
        self.assertListEqual(self.s_deque.deque, self.items_list[:-1])

    def test_many_items_remove_front(self):
        len_queue = self.s_deque.size()
        result_remove = self.s_deque.removeFront()
        self.assertEqual(self.s_deque.size(), len_queue - 1)
        self.assertEqual(result_remove, self.items_list[0])
        self.assertListEqual(self.s_deque.deque, self.items_list[1:])


class TestDequeCheckPalidrome(unittest.TestCase):

    def test_check_palidrome(self):
        true_words = ['kayak', 'deified', 'rotator', 'peep', 'wow']
        false_words = ['hello', 'defender', 'potato', 'hi', 'world']
        for i in range(len(true_words)):
            self.assertTrue(check_palidrome(true_words[i]))
            self.assertFalse(check_palidrome(false_words[i]))


if __name__ == '__main__':
    unittest.main()
