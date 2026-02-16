import random
import unittest
from typing import List

from LinkedList2 import LinkedList2, Node


class TestLinkedList2OneItem(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList2()
        self.number = random.randint(0, 100)
        self.node = Node(self.number)
        self.s_list.add_in_tail(self.node)

    def test_one_item_check_head_tail_len_prev_next(self):
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, self.s_list.tail)
        self.assertIsNone(self.node.next)
        self.assertIsNone(self.node.prev)

    def test_one_item_add_in_tail(self):
        new_node = Node(random.randint(0, 100))
        self.s_list.add_in_tail(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.head, self.node)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertEqual(self.node.next, new_node)
        self.assertIsNone(self.node.prev)
        self.assertEqual(new_node.prev, self.node)
        self.assertIsNone(new_node.next)

    def test_one_item_find(self):
        result = self.s_list.find(self.number)
        self.assertIsInstance(result, Node)
        self.assertEqual(result, self.node)

    def test_one_item_find_return_none(self):
        number = random.randint(101, 200)  # value not in s_list
        result = self.s_list.find(number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_one_item_find_all(self):
        result = self.s_list.find_all(self.number)
        self.assertIsInstance(result, List)
        self.assertEqual(len(result), 1)
        self.assertEqual(result, [self.node])

    def test_one_item_len(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_one_item_delete(self):
        self.s_list.delete(self.number)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_one_item_delete_all(self):
        self.s_list.delete(self.number, all=True)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_one_item_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_one_item_insert(self):
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(self.node, new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.head, self.node)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertEqual(self.s_list.head.next, self.s_list.tail)
        self.assertIsNone(self.s_list.head.prev)
        self.assertEqual(self.s_list.tail.prev, self.s_list.head)
        self.assertIsNone(self.s_list.tail.next)

    def test_one_item_add_in_head(self):
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.add_in_head(new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, tail)
        self.assertEqual(self.s_list.tail.prev, new_node)
        self.assertEqual(self.s_list.head.next, tail)
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)


class TestLinkedList2Empty(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList2()
        self.number = random.randint(0, 100)

    def test_empty_check_head_tail_len(self):
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_empty_add_in_tail(self):
        new_node = Node(self.number)
        self.s_list.add_in_tail(new_node)
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertIsNone(new_node.next)
        self.assertIsNone(new_node.prev)

    def test_empty_find(self):
        result = self.s_list.find(self.number)
        self.assertEqual(result, None)

    def test_one_item_find_all(self):
        result = self.s_list.find_all(self.number)
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

    def test_empty_delete_all(self):
        self.s_list.delete(self.number, all=True)
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_empty_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_empty_insert(self):
        new_node = Node(self.number)
        self.s_list.insert(None, new_node)
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertIsNone(self.s_list.head.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_empty_add_in_head(self):
        new_node = Node(self.number)
        self.s_list.add_in_head(new_node)
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertIsNone(self.s_list.head.next)
        self.assertIsNone(self.s_list.head.prev)


class TestLinkedListManyItems(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList2()
        number = random.randrange(3, 100)
        self.nodes_list = [Node(random.randint(0, 100)) for _ in range(number)]
        for node in self.nodes_list:
            self.s_list.add_in_tail(node)
        self.len_nodes_list = len(self.nodes_list)

    def test_many_items_check_head_tail_len_next_prev(self):
        self.assertEqual(self.s_list.len(), self.len_nodes_list)
        self.assertEqual(self.s_list.head, self.nodes_list[0])
        self.assertEqual(self.s_list.tail, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next, self.nodes_list[1])
        self.assertEqual(self.s_list.tail.prev, self.nodes_list[-2])

    def test_many_items_add_in_tail(self):
        new_node = Node(random.randint(0, 100))
        self.s_list.add_in_tail(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head, self.nodes_list[0])
        self.assertEqual(self.s_list.tail, new_node)
        self.assertEqual(new_node.prev, self.nodes_list[-1])
        self.assertIsNone(new_node.next)

    def test_many_items_find(self):
        node = random.choice(self.nodes_list)
        result = self.s_list.find(node.value)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.value, node.value)

    def test_many_items_find_return_none(self):
        number = random.randint(101, 200)  # value not in self.nodes_list
        result = self.s_list.find(number)
        self.assertIsInstance(result, type(None))
        self.assertEqual(result, None)

    def test_many_items_find_all(self):
        find_node = random.choice(self.nodes_list)
        check_list = (
            [node for node in self.nodes_list if node.value == find_node.value]
        )
        result = self.s_list.find_all(find_node.value)
        self.assertIsInstance(result, List)
        self.assertIsInstance(result[0], Node)
        self.assertEqual(result, check_list)

    def test_many_items_len(self):
        result = self.s_list.len()
        self.assertIsInstance(result, int)
        self.assertEqual(result, self.len_nodes_list)

    def test_many_items_delete_first_node(self):
        self.s_list.delete(self.s_list.head.value)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head, self.nodes_list[1])
        self.assertEqual(self.s_list.tail, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next, self.nodes_list[2])
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)
        self.assertEqual(self.s_list.tail.prev, self.nodes_list[-2])

    def test_many_items_delete_last_node(self):
        self.s_list.add_in_tail(Node(101))  # added in tail uniq value
        self.assertEqual(self.s_list.tail.value, 101)
        self.len_nodes_list += 1
        self.s_list.delete(self.s_list.tail.value)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head, self.nodes_list[0])
        self.assertEqual(self.s_list.tail, self.nodes_list[-1])
        self.assertEqual(self.s_list.head.next, self.nodes_list[1])
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)
        self.assertEqual(self.s_list.tail.prev, self.nodes_list[-2])

    def test_many_items_delete_middle_node(self):
        head = self.s_list.head
        tail = self.s_list.tail
        self.s_list.delete(self.s_list.head.next.value)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.tail, tail)
        self.assertEqual(self.s_list.head.next, self.nodes_list[2])
        self.assertEqual(self.s_list.head.next.prev, self.nodes_list[0])

    def test_many_items_delete_all_first_item(self):
        head_value = self.s_list.head.value
        node_value = self.nodes_list[0].value
        del_nodes = len(
            [node for node in self.nodes_list if node.value == node_value]
        )
        nodes_list_after_del = (
            [node for node in self.nodes_list if node.value != node_value]
        )
        self.s_list.delete(node_value, all=True)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - del_nodes)
        self.assertNotEqual(self.s_list.head.value, head_value)
        self.assertEqual(self.s_list.head, nodes_list_after_del[0])
        self.assertEqual(self.s_list.tail, nodes_list_after_del[-1])
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)
        self.assertEqual(self.s_list.head.next, nodes_list_after_del[1])
        self.assertEqual(self.s_list.tail.prev, nodes_list_after_del[-2])

    def test_many_items_delete_all_last_item(self):
        tail_value = self.s_list.tail
        node_value = self.nodes_list[-1].value
        del_nodes = len(
            [node for node in self.nodes_list if node.value == node_value]
        )
        nodes_list_after_del = (
            [node for node in self.nodes_list if node.value != node_value]
        )
        self.s_list.delete(node_value, all=True)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - del_nodes)
        self.assertNotEqual(self.s_list.tail.value, tail_value)
        self.assertEqual(self.s_list.head, nodes_list_after_del[0])
        self.assertEqual(self.s_list.tail, nodes_list_after_del[-1])
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)
        self.assertEqual(self.s_list.head.next, nodes_list_after_del[1])
        self.assertEqual(self.s_list.tail.prev, nodes_list_after_del[-2])

    def test_many_items_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_many_items_insert(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(None, new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertNotEqual(self.s_list.tail, tail)
        self.assertEqual(self.s_list.tail, new_node)
        self.assertEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.tail.prev, self.nodes_list[-1])
        self.assertIsNone(self.s_list.tail.next)
        self.assertIsNone(self.s_list.head.prev)

    def test_many_items_insert_middle_place(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(self.nodes_list[0], new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.tail, tail)
        self.assertEqual(self.s_list.head.next, new_node)
        self.assertEqual(new_node.prev, self.s_list.head)
        self.assertEqual(new_node.next, self.s_list.head.next.next)
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)

    def test_many_items_add_in_head(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.add_in_head(new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertNotEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, tail)
        self.assertEqual(self.s_list.head.next, head)
        self.assertIsNone(self.s_list.head.prev)
        self.assertIsNone(self.s_list.tail.next)


if __name__ == '__main__':
    unittest.main()
