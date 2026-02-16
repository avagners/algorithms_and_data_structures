import random
import unittest
from typing import List

from OrderedList import OrderedList, Node


class TestOrderedListOneItemAscTrue(unittest.TestCase):

    def setUp(self):
        self.s_list = OrderedList(asc=True)
        self.number = random.randint(50, 100)
        self.s_list.add(self.number)

    def test_one_item_check_head_tail_len_prev_next_asc_true(self):
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, self.s_list.tail)
        self.assertIsNone(self.s_list.head.next)
        self.assertIsNone(self.s_list.tail.prev)
        self.assertTrue(self.s_list.is_asc())

    def test_one_item_add_greater_asc_true(self):
        new_node = random.randint(100, 200)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.tail.prev, self.s_list.head)
        self.assertEqual(self.s_list.head.next, self.s_list.tail)
        self.assertEqual(self.s_list.head.value, self.number)
        self.assertEqual(self.s_list.tail.value, new_node)
        self.assertEqual(self.s_list.head.next.value, new_node)
        self.assertEqual(self.s_list.tail.prev.value, self.s_list.head.value)
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertGreaterEqual(self.s_list.tail.value, self.s_list.head.value)

    def test_one_item_add_less_asc_true(self):
        new_node = random.randint(0, 50)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.tail.prev, self.s_list.head)
        self.assertEqual(self.s_list.head.next, self.s_list.tail)
        self.assertEqual(self.s_list.head.value, new_node)
        self.assertEqual(self.s_list.tail.value, self.number)
        self.assertEqual(self.s_list.head.next.value, self.number)
        self.assertEqual(self.s_list.tail.prev.value, new_node)
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)
        self.assertGreaterEqual(self.s_list.tail.value, self.s_list.head.value)

    def test_one_item_find_asc_true(self):
        result = self.s_list.find(self.number)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.value, self.number)

    def test_one_item_find_return_none_asc_true(self):
        number = random.randint(101, 200)  # value not in s_list
        result = self.s_list.find(number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_one_item_get_all_asc_true(self):
        result = self.s_list.get_all()
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), 1)

    def test_one_item_len_asc_true(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_one_item_delete_asc_true(self):
        self.s_list.delete(self.number)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_one_item_clean_asc_true(self):
        self.s_list.clean(asc=False)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)
        self.assertFalse(self.s_list.is_asc())


class TestOrderedListOneItemAscFalse(unittest.TestCase):

    def setUp(self):
        self.s_list = OrderedList(asc=False)
        self.number = random.randint(50, 100)
        self.s_list.add(self.number)

    def test_one_item_check_head_tail_len_prev_next_asc_false(self):
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, self.s_list.tail)
        self.assertIsNone(self.s_list.head.next)
        self.assertIsNone(self.s_list.tail.prev)
        self.assertFalse(self.s_list.is_asc())

    def test_one_item_add_greater_asc_false(self):
        new_node = random.randint(100, 200)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.tail.prev, self.s_list.head)
        self.assertEqual(self.s_list.head.next, self.s_list.tail)
        self.assertEqual(self.s_list.head.value, new_node)
        self.assertEqual(self.s_list.tail.value, self.number)
        self.assertEqual(self.s_list.head.next.value, self.s_list.tail.value)
        self.assertEqual(self.s_list.tail.prev.value, new_node)
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertLessEqual(self.s_list.tail.value, self.s_list.head.value)

    def test_one_item_add_less_asc_false(self):
        new_node = random.randint(0, 50)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.tail.prev, self.s_list.head)
        self.assertEqual(self.s_list.head.next, self.s_list.tail)
        self.assertEqual(self.s_list.head.value, self.number)
        self.assertEqual(self.s_list.tail.value, new_node)
        self.assertEqual(self.s_list.head.next.value, new_node)
        self.assertEqual(self.s_list.tail.prev.value, self.number)
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)
        self.assertLessEqual(self.s_list.tail.value, self.s_list.head.value)

    def test_one_item_find_asc_false(self):
        result = self.s_list.find(self.number)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.value, self.number)

    def test_one_item_find_return_none_asc_false(self):
        number = random.randint(101, 200)  # value not in s_list
        result = self.s_list.find(number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_one_item_get_all_asc_false(self):
        result = self.s_list.get_all()
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), 1)

    def test_one_item_len_asc_false(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_one_item_delete_asc_false(self):
        self.s_list.delete(self.number)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_one_item_clean_asc_false(self):
        self.s_list.clean(asc=False)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)
        self.assertFalse(self.s_list.is_asc())


class TestOrderedListEmpty(unittest.TestCase):

    def setUp(self):
        self.s_list = OrderedList(asc=True)
        self.number = random.randint(0, 100)

    def test_empty_check_head_tail_len(self):
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)
        self.assertTrue(self.s_list.is_asc())

    def test_empty_add(self):
        new_node = self.number
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head.value, new_node)
        self.assertEqual(self.s_list.tail.value, new_node)
        self.assertIsNone(self.s_list.head.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_empty_find(self):
        result = self.s_list.find(self.number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_empty_get_all(self):
        result = self.s_list.get_all()
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_empty_len(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_empty_delete(self):
        self.s_list.delete(self.number)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_empty_clean(self):
        self.s_list.clean(asc=False)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)
        self.assertFalse(self.s_list.is_asc())


class TestOrderedListManyItemsAscTrue(unittest.TestCase):

    def setUp(self):
        self.s_list = OrderedList(asc=True)
        number = random.randrange(3, 100)
        self.nodes_list = [random.randint(50, 100) for _ in range(number)]
        self.nodes_list.sort()
        for node in self.nodes_list:
            self.s_list.add(node)
        self.len_nodes_list = len(self.nodes_list)

    def test_many_items_check_head_tail_len_next_prev_asc_true(self):
        self.assertEqual(self.s_list.len(), self.len_nodes_list)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next.value, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.prev.value, self.nodes_list[-2])
        s_list_values = [node.value for node in self.s_list.get_all()]
        self.assertListEqual(s_list_values, self.nodes_list)
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertTrue(self.s_list.is_asc())

    def test_many_items_add_head_asc_true(self):
        new_node = random.randint(0, 50)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head.value, new_node)
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.prev.value, self.nodes_list[-2])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertLessEqual(
            self.s_list.head.value, self.s_list.head.next.value
        )
        s_list_values = [node.value for node in self.s_list.get_all()]
        self.assertListEqual(s_list_values[1:], self.nodes_list)

    def test_many_items_add_tail_asc_true(self):
        new_node = random.randint(100, 150)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, new_node)
        self.assertEqual(self.s_list.head.next.value, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.prev.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertLessEqual(
            self.s_list.head.value, self.s_list.head.next.value
        )
        s_list_values = [node.value for node in self.s_list.get_all()]
        self.assertListEqual(s_list_values[:-1], self.nodes_list)

    def test_many_items_add_middle_asc_true(self):
        new_node = self.nodes_list[0] + 1
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_find_asc_true(self):
        number = random.choice(self.nodes_list)
        result = self.s_list.find(number)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.value, number)

    def test_many_items_find_return_none_asc_true(self):
        number = random.randint(101, 200)  # value not in s_list
        result = self.s_list.find(number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_many_items_get_all_asc_true(self):
        result = self.s_list.get_all()
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), self.len_nodes_list)
        s_list_values = [node.value for node in result]
        self.assertListEqual(s_list_values, self.nodes_list)

    def test_many_items_len_asc_true(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, self.len_nodes_list)

    def test_many_items_delete_first_item_asc_true(self):
        number = self.nodes_list[0]
        self.s_list.delete(number)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[1])
        self.assertEqual(self.s_list.head.next.prev.value, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_delete_last_item_asc_true(self):
        number = self.nodes_list[-1]
        self.s_list.delete(number)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-2])
        self.assertEqual(self.s_list.tail.prev.next.value, self.nodes_list[-2])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_delete_middle_item_asc_true(self):
        number = random.choice(self.nodes_list[1:-1])
        self.s_list.delete(number)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_clean_asc_true(self):
        self.s_list.clean(asc=False)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)
        self.assertFalse(self.s_list.is_asc())


class TestOrderedListManyItemsAscFalse(unittest.TestCase):

    def setUp(self):
        self.s_list = OrderedList(asc=False)
        number = random.randrange(3, 100)
        self.nodes_list = [random.randint(50, 100) for _ in range(number)]
        self.nodes_list.sort(reverse=True)
        for node in self.nodes_list:
            self.s_list.add(node)
        self.len_nodes_list = len(self.nodes_list)

    def test_many_items_check_head_tail_len_next_prev_asc_false(self):
        self.assertEqual(self.s_list.len(), self.len_nodes_list)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next.value, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.prev.value, self.nodes_list[-2])
        s_list_values = [node.value for node in self.s_list.get_all()]
        self.assertListEqual(s_list_values, self.nodes_list)
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertFalse(self.s_list.is_asc())

    def test_many_items_add_head_asc_false(self):
        new_node = random.randint(100, 150)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head.value, new_node)
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.prev.value, self.nodes_list[-2])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertGreaterEqual(
            self.s_list.head.value, self.s_list.head.next.value
        )
        s_list_values = [node.value for node in self.s_list.get_all()]
        self.assertListEqual(s_list_values[1:], self.nodes_list)

    def test_many_items_add_tail_asc_false(self):
        new_node = random.randint(0, 50)
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, new_node)
        self.assertEqual(self.s_list.head.next.value, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.prev.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertLessEqual(
            self.s_list.tail.value, self.s_list.tail.prev.value
        )
        s_list_values = [node.value for node in self.s_list.get_all()]
        self.assertListEqual(s_list_values[:-1], self.nodes_list)

    def test_many_items_add_middle_asc_false(self):
        new_node = self.nodes_list[0] - 1
        self.s_list.add(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_find_asc_false(self):
        number = random.choice(self.nodes_list)
        result = self.s_list.find(number)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.value, number)

    def test_many_items_find_return_none_asc_false(self):
        number = random.randint(101, 200)  # value not in s_list
        result = self.s_list.find(number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_many_items_get_all_asc_false(self):
        result = self.s_list.get_all()
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), self.len_nodes_list)
        s_list_values = [node.value for node in result]
        self.assertListEqual(s_list_values, self.nodes_list)

    def test_many_items_len_asc_false(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, self.len_nodes_list)

    def test_many_items_delete_first_item_asc_false(self):
        number = self.nodes_list[0]
        self.s_list.delete(number)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[1])
        self.assertEqual(self.s_list.head.next.prev.value, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_delete_last_item_asc_false(self):
        number = self.nodes_list[-1]
        self.s_list.delete(number)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-2])
        self.assertEqual(self.s_list.tail.prev.next.value, self.nodes_list[-2])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_delete_middle_item_asc_false(self):
        number = random.choice(self.nodes_list[1:-1])
        self.s_list.delete(number)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head.value, self.nodes_list[0])
        self.assertEqual(self.s_list.tail.value, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_clean_asc_false(self):
        self.s_list.clean(asc=True)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)
        self.assertTrue(self.s_list.is_asc())


if __name__ == '__main__':
    unittest.main()
