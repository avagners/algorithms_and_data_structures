import random
import unittest

from LinkedList import LinkedList, Node
from sum_two_linked_list import sum_nodes_two_lists


class TestLinkedListOneItem(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList()
        self.number = random.randint(0, 100)
        self.node = Node(self.number)
        self.s_list.add_in_tail(self.node)

    def test_one_item_check_head_tail_len(self):
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head.value, self.number)
        self.assertEqual(self.s_list.tail.value, self.number)

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

    def test_one_item_find_all(self):
        find_list = self.s_list.find_all(self.number)
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(len(find_list), 1)
        self.assertEqual(find_list, [self.node])

    def test_one_item_len(self):
        self.assertEqual(self.s_list.len(), 1)

    def test_one_item_insert(self):
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(self.node, new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertEqual(self.s_list.head, self.node)
        self.assertEqual(self.s_list.tail, new_node)

    def test_one_item_insert_first_place(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(None, new_node)
        self.assertEqual(self.s_list.len(), 2)
        self.assertNotEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, tail)


class TestLinkedListEmpty(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList()
        self.number = random.randint(0, 100)

    def test_empty_check_head_tail_len(self):
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

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

    def test_empty_find_all(self):
        find_list = self.s_list.find_all(self.number)
        self.assertEqual(self.s_list.len(), 0)
        self.assertEqual(len(find_list), 0)
        self.assertEqual(find_list, [])

    def test_empty_len(self):
        self.assertEqual(self.s_list.len(), 0)

    def test_empty_insert(self):
        new_node = Node(self.number)
        self.s_list.insert(None, new_node)
        self.assertEqual(self.s_list.len(), 1)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, new_node)


class TestLinkedListManyItems(unittest.TestCase):

    def setUp(self):
        self.s_list = LinkedList()
        number = random.randrange(2, 100)
        self.nodes_list = [Node(random.randint(0, 100)) for _ in range(number)]
        for node in self.nodes_list:
            self.s_list.add_in_tail(node)
        self.len_nodes_list = len(self.nodes_list)

    def test_many_items_check_head_tail_len(self):
        self.assertEqual(self.s_list.len(), self.len_nodes_list)
        self.assertEqual(self.s_list.head, self.nodes_list[0])
        self.assertEqual(self.s_list.tail, self.nodes_list[-1])

    def test_many_items_delete_first_node(self):
        self.s_list.delete(self.nodes_list[0].value)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head, self.nodes_list[1])
        self.assertEqual(self.s_list.tail, self.nodes_list[-1])

    def test_many_items_delete_last_node(self):
        self.s_list.add_in_tail(Node(101))  # added in tail uniq value
        self.assertEqual(self.s_list.tail.value, 101)
        self.len_nodes_list += 1
        self.s_list.delete(self.s_list.tail.value)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head, self.nodes_list[0])
        self.assertEqual(self.s_list.tail, self.nodes_list[-1])

    def test_many_items_delete_middle_node(self):
        head = self.s_list.head
        tail = self.s_list.tail
        self.s_list.insert(head, Node(101))  # added in middle uniq value
        self.len_nodes_list += 1
        self.s_list.delete(101)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - 1)
        self.assertEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.tail, tail)

    def test_many_items_delete_all_first_item(self):
        head_value = self.s_list.head.value
        node_value = self.nodes_list[0].value
        del_nodes = len(
            [node for node in self.nodes_list if node.value == node_value]
        )
        list_after_del = (
            [node for node in self.nodes_list if node.value != node_value]
        )
        self.s_list.delete(node_value, all=True)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - del_nodes)
        self.assertNotEqual(self.s_list.head.value, head_value)
        self.assertEqual(self.s_list.head, list_after_del[0])
        self.assertEqual(self.s_list.tail, list_after_del[-1])

    def test_many_items_delete_all_last_item(self):
        tail_value = self.s_list.tail
        node_value = self.nodes_list[-1].value
        del_nodes = len(
            [node for node in self.nodes_list if node.value == node_value]
        )
        list_after_del = (
            [node for node in self.nodes_list if node.value != node_value]
        )
        self.s_list.delete(node_value, all=True)
        self.assertEqual(self.s_list.len(), self.len_nodes_list - del_nodes)
        self.assertNotEqual(self.s_list.tail.value, tail_value)
        self.assertEqual(self.s_list.head, list_after_del[0])
        self.assertEqual(self.s_list.tail, list_after_del[-1])

    def test_many_items_clean(self):
        self.s_list.clean()
        self.assertEqual(self.s_list.len(), 0)
        self.assertIsNone(self.s_list.head)
        self.assertIsNone(self.s_list.tail)

    def test_many_items_find_all(self):
        node_value = random.choice(self.nodes_list)
        result_list = (
            [node for node in self.nodes_list if node.value == node_value]
        )
        count_node_value_in_list = len(result_list)
        find_list = self.s_list.find_all(node_value)
        self.assertEqual(self.s_list.len(), self.len_nodes_list)
        self.assertEqual(len(find_list), count_node_value_in_list)
        self.assertListEqual(find_list, result_list)

    def test_many_items_len(self):
        self.assertEqual(self.s_list.len(), self.len_nodes_list)

    def test_many_items_insert_first_place(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(None, new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertNotEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.head, new_node)
        self.assertEqual(self.s_list.tail, tail)

    def test_many_items_insert_last_place(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(self.nodes_list[-1], new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertNotEqual(self.s_list.tail, tail)
        self.assertEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.tail, new_node)

    def test_many_items_insert_middle_place(self):
        head = self.s_list.head
        tail = self.s_list.tail
        new_node = Node(random.randint(0, 100))
        self.s_list.insert(self.nodes_list[2], new_node)
        self.assertEqual(self.s_list.len(), self.len_nodes_list + 1)
        self.assertEqual(self.s_list.head, head)
        self.assertEqual(self.s_list.tail, tail)


class TestSumNodesTwoLinkedLists(unittest.TestCase):

    def setUp(self):
        number = random.randrange(2, 100)

        self.nodes_list_1 = (
            [Node(random.randint(0, 100)) for _ in range(number)]
        )
        self.s_list_1 = LinkedList()
        for node in self.nodes_list_1:
            self.s_list_1.add_in_tail(node)

        self.nodes_list_2 = (
            [Node(random.randint(0, 100)) for _ in range(number)]
        )
        self.s_list_2 = LinkedList()
        for node in self.nodes_list_2:
            self.s_list_2.add_in_tail(node)

    def test_sum_two_list(self):
        zipped_nodes = zip(self.nodes_list_1, self.nodes_list_2)
        sum_two_list = (
            [node_1.value + node_2.value for node_1, node_2 in zipped_nodes]
        )
        result_function = sum_nodes_two_lists(self.s_list_1, self.s_list_2)
        self.assertListEqual(result_function, sum_two_list)

    def test_return_none_if_diff_len(self):
        new_node = Node(random.randint(0, 100))
        self.s_list_1.add_in_tail(new_node)
        result_function = sum_nodes_two_lists(self.s_list_1, self.s_list_2)
        self.assertIsNone(result_function)


if __name__ == '__main__':
    unittest.main()
