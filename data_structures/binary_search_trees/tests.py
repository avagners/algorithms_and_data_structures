import unittest

from binary_search_tree import BSTNode, BSTFind, BST


class TestBSTree(unittest.TestCase):

    def setUp(self):
        self.tree = BST(None)

    def test_tree(self):
        self.assertIsInstance(self.tree, BST)
        self.assertIsNone(self.tree.Root)

    def test_node(self):
        node = BSTNode(key=1, val=1, parent=None)
        self.assertIsInstance(node, BSTNode)
        self.assertEqual(node.NodeKey, 1)
        self.assertEqual(node.NodeValue, 1)
        self.assertIsNone(node.Parent)

    def test_find_node(self):
        # нет ни одного узла
        search_result = self.tree.FindNodeByKey(1)
        self.assertIsInstance(search_result, BSTFind)
        self.assertIsNone(search_result.Node)
        self.assertFalse(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)
        # добавили корень
        self.tree.AddKeyValue(10, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        # запрошенный ключ добавляем левому потомку
        search_result = self.tree.FindNodeByKey(8)
        self.assertEqual(search_result.Node.NodeKey, 10)
        self.assertTrue(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)
        # запрошенный ключ добавляем правому потомку
        search_result = self.tree.FindNodeByKey(12)
        self.assertEqual(search_result.Node.NodeKey, 10)
        self.assertFalse(search_result.ToLeft)
        self.assertFalse(search_result.NodeHasKey)
        self.tree.AddKeyValue(8, 1)
        # проверяем поиск присутствующего ключа
        search_result = self.tree.FindNodeByKey(8)
        self.assertEqual(search_result.Node.NodeKey, 8)
        self.assertFalse(search_result.ToLeft)
        self.assertTrue(search_result.NodeHasKey)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 8)

    def test_add_root_node(self):
        self.assertIsNone(self.tree.FindNodeByKey(10).Node)
        self.tree.AddKeyValue(10, 1)
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsInstance(self.tree.Root, BSTNode)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)

    def test_add_many_nodes(self):
        self.assertIsNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNone(self.tree.FindNodeByKey(8).Node)
        self.assertIsNone(self.tree.FindNodeByKey(12).Node)
        self.tree.AddKeyValue(10, 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNotNone(self.tree.FindNodeByKey(8).Node)
        self.assertIsNotNone(self.tree.FindNodeByKey(12).Node)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsInstance(self.tree.Root.LeftChild, BSTNode)
        self.assertIsInstance(self.tree.Root.RightChild, BSTNode)
        self.assertLess(
            self.tree.Root.LeftChild.NodeKey, self.tree.Root.NodeKey
        )
        self.assertGreater(
            self.tree.Root.RightChild.NodeKey, self.tree.Root.NodeKey
        )
        self.assertEqual(
            self.tree.Root.LeftChild.Parent.NodeKey, self.tree.Root.NodeKey
        )
        self.assertEqual(
            self.tree.Root.RightChild.Parent.NodeKey, self.tree.Root.NodeKey
        )

    def test_add_identical_keys(self):
        self.assertIsNone(self.tree.FindNodeByKey(10).Node)
        self.tree.AddKeyValue(10, 1)
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        # при попытке добавить узел с таким же ключом
        # дерево не изменяется
        self.tree.AddKeyValue(10, 2)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)

    def test_find_min_max(self):
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertIsNone(result)
        self.tree.AddKeyValue(10, 1)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(result.NodeKey, 10)
        result = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(result.NodeKey, 10)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(result.NodeKey, 12)
        result = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(result.NodeKey, 8)
        result = self.tree.FinMinMax(self.tree.Root.LeftChild, True)
        self.assertEqual(result.NodeKey, 8)
        result = self.tree.FinMinMax(self.tree.Root.RightChild, False)
        self.assertEqual(result.NodeKey, 12)
        self.tree.AddKeyValue(5, 4)
        self.tree.AddKeyValue(16, 5)
        result = self.tree.FinMinMax(self.tree.Root, False)
        self.assertEqual(result.NodeKey, 5)
        result = self.tree.FinMinMax(self.tree.Root, True)
        self.assertEqual(result.NodeKey, 16)
        result = self.tree.FinMinMax(self.tree.Root.RightChild, False)
        self.assertEqual(result.NodeKey, 12)
        result = self.tree.FinMinMax(self.tree.Root.RightChild, True)
        self.assertEqual(result.NodeKey, 16)
        result = self.tree.FinMinMax(self.tree.Root.LeftChild, False)
        self.assertEqual(result.NodeKey, 5)
        result = self.tree.FinMinMax(self.tree.Root.LeftChild, True)
        self.assertEqual(result.NodeKey, 8)

    def test_get_count(self):
        self.assertEqual(self.tree.Count(), 0)
        self.tree.AddKeyValue(10, 1)
        self.assertEqual(self.tree.Count(), 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.assertEqual(self.tree.Count(), 3)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))


class TestDeleteNode(unittest.TestCase):

    def setUp(self):
        self.tree = BST(None)
        self.tree.AddKeyValue(10, 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.tree.AddKeyValue(5, 4)
        self.tree.AddKeyValue(16, 5)
        self.tree.AddKeyValue(13, 6)
        self.tree.AddKeyValue(18, 7)
        self.tree.AddKeyValue(9, 8)
        self.tree.AddKeyValue(11, 9)

    def test_tree(self):
        # проверяем удаляемый узел и соседние узлы до удаления
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 12)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 16)
        self.assertEqual(self.tree.Root.RightChild.RightChild.Parent.NodeKey, 12)
        self.assertEqual(self.tree.Root.RightChild.RightChild.LeftChild.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.RightChild.RightChild.NodeKey, 18)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 12)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)

    def test_successor_is_leaf(self):
        # наследник не имеет наследников
        size_tree = self.tree.Count()
        delete_node = self.tree.FindNodeByKey(12)
        self.tree.DeleteNodeByKey(12)
        all_nodes = self.tree.GetAllNodes()
        self.assertNotIn(delete_node, all_nodes)
        self.assertEqual(self.tree.Count(), size_tree - 1)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 16)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.RightChild.Parent.NodeKey, 13)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.LeftChild)
        self.assertEqual(self.tree.Root.RightChild.RightChild.RightChild.NodeKey, 18)

    def test_successor_has_right_node(self):
        # у преемника есть правый наследник
        self.tree.AddKeyValue(15, 10)
        size_tree = self.tree.Count()
        delete_node = self.tree.FindNodeByKey(12)
        self.tree.DeleteNodeByKey(12)
        all_nodes = self.tree.GetAllNodes()
        self.assertNotIn(delete_node, all_nodes)
        self.assertEqual(self.tree.Count(), size_tree - 1)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 16)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.RightChild.Parent.NodeKey, 13)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        # на место преемника поместили его правого наследника
        self.assertEqual(self.tree.Root.RightChild.RightChild.LeftChild.NodeKey, 15)
        self.assertEqual(self.tree.Root.RightChild.RightChild.LeftChild.Parent.NodeKey, 16)
        self.assertEqual(self.tree.Root.RightChild.RightChild.RightChild.NodeKey, 18)

    def test_delte_root(self):
        size = self.tree.Count()
        node = self.tree.FindNodeByKey(10).Node
        self.assertIn(node, self.tree.GetAllNodes())
        self.tree.DeleteNodeByKey(10)
        self.assertNotIn(node, self.tree.GetAllNodes())
        self.assertEqual(self.tree.Root.NodeKey, 11)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 8)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 12)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 11)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 11)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertEqual(self.tree.Count(), size - 1)

    def test_if_not_find_node(self):
        size_tree = self.tree.Count()
        self.assertFalse(self.tree.DeleteNodeByKey(100))
        self.assertEqual(self.tree.Count(), size_tree)


if __name__ == '__main__':
    unittest.main()