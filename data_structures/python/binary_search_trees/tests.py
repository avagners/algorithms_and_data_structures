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
        self.assertTrue(self.tree.AddKeyValue(10, 1))
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
        self.assertTrue(self.tree.AddKeyValue(10, 1))
        self.assertTrue(self.tree.AddKeyValue(8, 2))
        self.assertTrue(self.tree.AddKeyValue(12, 3))
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
        self.assertTrue(self.tree.AddKeyValue(10, 1))
        self.assertIsNotNone(self.tree.FindNodeByKey(10).Node)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertIsNone(self.tree.Root.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild)
        self.assertEqual(self.tree.Root.NodeValue, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        # при попытке добавить узел с таким же ключом
        # дерево не изменяется
        self.assertFalse(self.tree.AddKeyValue(10, 2))
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

    def test_delete_last_node(self):
        self.tree.AddKeyValue(10, 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.tree.AddKeyValue(11, 3)
        self.assertTrue(self.tree.DeleteNodeByKey(11))
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 8)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 12)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild)
        self.assertEqual(self.tree.Count(), 3)

    def test_delete_only_root(self):
        # удаляем корень дерева состоящего из 1-го узла
        self.assertIsNone(self.tree.Root)
        self.tree.AddKeyValue(10, 1)
        self.assertEqual(self.tree.Root.NodeKey, 10)
        node = self.tree.FindNodeByKey(10).Node
        self.assertEqual(node, self.tree.Root)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertTrue(self.tree.DeleteNodeByKey(10))
        self.assertEqual(self.tree.Count(), len(all_nodes) - 1)
        all_nodes = self.tree.GetAllNodes()
        self.assertNotIn(node, all_nodes)
        self.assertIsNone(self.tree.Root)

    def test_delete_root(self):
        # удаляем корень дерева состоящего из 3-х узлов
        # родитель преемника = удаляемый корень
        # у преемника нет потомоков
        self.tree.AddKeyValue(50, 1)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.tree.AddKeyValue(25, 2)
        self.tree.AddKeyValue(75, 2)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 50)
        self.assertTrue(self.tree.DeleteNodeByKey(50))
        self.assertEqual(self.tree.Count(), len(all_nodes) - 1)
        self.assertIsNone(self.tree.Root.Parent)
        self.assertEqual(self.tree.Root.NodeKey, 75)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 75)
        self.assertIsNone(self.tree.Root.RightChild)

    def test_delete_root_with_right_child(self):
        # удаляем корень дерева из 4-х узлов
        # родитель преемника = удаляемый корень
        # у преемника есть правый потомок
        self.tree.AddKeyValue(50, 1)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.tree.AddKeyValue(25, 2)
        self.tree.AddKeyValue(75, 2)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 50)
        # добавляем правого потомка для преемника
        self.tree.AddKeyValue(100, 3)
        self.assertEqual(self.tree.Count(), len(all_nodes) + 1)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 100)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 75
        )
        self.assertTrue(self.tree.DeleteNodeByKey(50))
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.NodeKey, 75)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 75)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 100)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 75)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)

    def test_delete_root_and_node_successor_is_leaf(self):
        # удаляем корень дерева из 5-ти узлов
        # преемник не имеет потомков
        self.tree.AddKeyValue(50, 1)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.tree.AddKeyValue(25, 2)
        self.tree.AddKeyValue(75, 2)
        self.tree.AddKeyValue(100, 3)
        self.tree.AddKeyValue(60, 3)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertTrue(self.tree.DeleteNodeByKey(50))
        self.assertEqual(self.tree.Count(), len(all_nodes) - 1)
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.NodeKey, 60)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 60)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 60)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 100)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 75
        )

    def test_delete_root_and_node_successor_is_not_leaf(self):
        # удаляем корень дерева из 6-ти узлов
        # у преемника есть правый потомок
        self.tree.AddKeyValue(50, 1)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.tree.AddKeyValue(25, 2)
        self.tree.AddKeyValue(75, 2)
        self.tree.AddKeyValue(100, 3)
        self.tree.AddKeyValue(60, 3)
        self.tree.AddKeyValue(65, 3)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertTrue(self.tree.DeleteNodeByKey(50))
        self.assertEqual(self.tree.Count(), len(all_nodes) - 1)
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.NodeKey, 60)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 60)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 75)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 60)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 65)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 100)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.RightChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 75
        )
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 75
        )

    def test_node_successor_parent_is_node_delete_leaf(self):
        self.tree.AddKeyValue(50, 1)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.tree.AddKeyValue(25, 2)
        self.tree.AddKeyValue(75, 2)
        self.tree.AddKeyValue(100, 3)
        self.tree.AddKeyValue(60, 3)
        self.tree.AddKeyValue(65, 3)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertTrue(self.tree.DeleteNodeByKey(75))
        self.assertEqual(self.tree.Count(), len(all_nodes) - 1)
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 100)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 50)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 60)
        self.assertIsNone(self.tree.Root.RightChild.RightChild)
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.RightChild.NodeKey, 65
        )
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 100
        )

    def test_node_successor_parent_is_node_delete_not_leaf(self):
        self.tree.AddKeyValue(50, 1)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.tree.AddKeyValue(25, 2)
        self.tree.AddKeyValue(75, 2)
        self.tree.AddKeyValue(100, 3)
        self.tree.AddKeyValue(120, 4)
        self.tree.AddKeyValue(60, 3)
        self.tree.AddKeyValue(65, 4)
        all_nodes = self.tree.GetAllNodes()
        self.assertEqual(self.tree.Count(), len(all_nodes))
        self.assertTrue(self.tree.DeleteNodeByKey(75))
        self.assertEqual(self.tree.Count(), len(all_nodes) - 1)
        self.assertEqual(self.tree.Root.Parent, None)
        self.assertEqual(self.tree.Root.NodeKey, 50)
        self.assertEqual(self.tree.Root.LeftChild.NodeKey, 25)
        self.assertIsNone(self.tree.Root.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.LeftChild.Parent.NodeKey, 50)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 100)
        self.assertEqual(self.tree.Root.RightChild.Parent.NodeKey, 50)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 60)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 120)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 100
        )
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.RightChild.NodeKey, 65
        )
        self.assertIsNone(
            self.tree.Root.RightChild.LeftChild.LeftChild
        )
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 100
        )

    def test_wide_all_nodes_in_empty_tree(self):
        all_nodes = self.tree.WideAllNodes()
        self.assertIsInstance(all_nodes, tuple)
        self.assertEqual(len(all_nodes), 0)

    def test_wide_all_nodes_only_root_node(self):
        self.tree.AddKeyValue(10, 1)
        all_nodes = self.tree.WideAllNodes()
        self.assertIsInstance(all_nodes, tuple)
        self.assertIsInstance(all_nodes[0], BSTNode)
        self.assertEqual(len(all_nodes), 1)


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
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 12
        )
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 16)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 12
        )
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.LeftChild.NodeKey, 13
        )
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.RightChild.NodeKey, 18
        )
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 12
        )
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)

    def test_successor_is_leaf(self):
        # преемник не имеет потомков
        size_tree = self.tree.Count()
        delete_node = self.tree.FindNodeByKey(12)
        self.assertTrue(self.tree.DeleteNodeByKey(12))
        all_nodes = self.tree.GetAllNodes()
        self.assertNotIn(delete_node, all_nodes)
        self.assertEqual(self.tree.Count(), size_tree - 1)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 16)
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 13
        )
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 13
        )
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(self.tree.Root.RightChild.RightChild.LeftChild)
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.RightChild.NodeKey, 18
        )

    def test_successor_has_right_node(self):
        # у преемника есть правый потомок
        self.tree.AddKeyValue(15, 10)
        size_tree = self.tree.Count()
        delete_node = self.tree.FindNodeByKey(12)
        self.assertTrue(self.tree.DeleteNodeByKey(12))
        all_nodes = self.tree.GetAllNodes()
        self.assertNotIn(delete_node, all_nodes)
        self.assertEqual(self.tree.Count(), size_tree - 1)
        self.assertEqual(self.tree.Root.RightChild.NodeKey, 13)
        self.assertEqual(self.tree.Root.RightChild.LeftChild.NodeKey, 11)
        self.assertEqual(self.tree.Root.RightChild.RightChild.NodeKey, 16)
        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey, 13
        )
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.Parent.NodeKey, 13
        )
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(self.tree.Root.RightChild.LeftChild.RightChild)
        # на место преемника поместили его правого потомка
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.LeftChild.NodeKey, 15
        )
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.LeftChild.Parent.NodeKey, 16
        )
        self.assertEqual(
            self.tree.Root.RightChild.RightChild.RightChild.NodeKey, 18
        )

    def test_delete_root(self):
        # удаляем корень в дереве
        # преемником не имеет потомков
        size = self.tree.Count()
        node = self.tree.FindNodeByKey(10).Node
        self.assertIn(node, self.tree.GetAllNodes())
        self.assertTrue(self.tree.DeleteNodeByKey(10))
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

    def test_delete_right_leaf(self):
        # удаляем правый последний узел
        node = self.tree.FindNodeByKey(18).Node
        node_parent = node.Parent
        self.assertEqual(node_parent.RightChild, node)
        self.assertEqual(node_parent.RightChild.NodeKey, 18)
        self.assertEqual(node_parent.NodeKey, 16)
        self.assertIn(node, self.tree.GetAllNodes())
        self.assertEqual(self.tree.Count(), 9)
        self.assertTrue(self.tree.DeleteNodeByKey(18))
        self.assertNotIn(node, self.tree.GetAllNodes())
        self.assertEqual(self.tree.Count(), 8)
        self.assertIsNone(node_parent.RightChild)
        self.assertIsNotNone(node_parent.LeftChild)

    def test_delete_left_leaf(self):
        # удаляем левый последний узел
        node = self.tree.FindNodeByKey(13).Node
        node_parent = node.Parent
        self.assertEqual(node_parent.LeftChild, node)
        self.assertEqual(node_parent.RightChild.NodeKey, 18)
        self.assertEqual(node_parent.NodeKey, 16)
        self.assertIn(node, self.tree.GetAllNodes())
        self.assertEqual(self.tree.Count(), 9)
        self.assertTrue(self.tree.DeleteNodeByKey(13))
        self.assertNotIn(node, self.tree.GetAllNodes())
        self.assertEqual(self.tree.Count(), 8)
        self.assertIsNone(node_parent.LeftChild)
        self.assertIsNotNone(node_parent.RightChild)
        self.assertEqual(node_parent.RightChild.NodeKey, 18)

    def test_delete_last_node(self):
        # удаляем последний узел
        node_parent = self.tree.FindNodeByKey(13).Node
        node = BSTNode(15, 10, node_parent)
        node_parent.RightChild = node
        self.assertEqual(node_parent.RightChild, node)
        self.assertEqual(node_parent.LeftChild, None)
        self.assertEqual(node_parent.RightChild.NodeKey, 15)
        self.assertEqual(node_parent.NodeKey, 13)
        self.assertEqual(node.Parent, node_parent)
        self.assertIn(node, self.tree.GetAllNodes())
        self.assertTrue(self.tree.DeleteNodeByKey(15))
        self.assertNotIn(node, self.tree.GetAllNodes())
        self.assertIsNone(node_parent.RightChild)
        self.assertIsNone(node_parent.LeftChild)

    def test_wide_all_nodes(self):
        all_nodes = self.tree.WideAllNodes()
        self.assertIsInstance(all_nodes, tuple)
        self.assertIsInstance(all_nodes[0], BSTNode)
        self.assertEqual(len(all_nodes), self.tree.Count())


class TestDeleteRoot(unittest.TestCase):

    def test_delete_root(self):
        root = BSTNode(8, 0, None)
        tree = BST(root)
        self.assertEqual(tree.Root.NodeKey, 8)
        node = tree.FindNodeByKey(8).Node
        self.assertEqual(node, tree.Root)
        all_nodes = tree.GetAllNodes()
        self.assertEqual(tree.Count(), len(all_nodes))
        self.assertTrue(tree.DeleteNodeByKey(8))
        self.assertEqual(tree.Count(), len(all_nodes) - 1)
        all_nodes = tree.GetAllNodes()
        self.assertNotIn(node, all_nodes)
        self.assertIsNone(tree.Root)


class TestDeepAllNodes(unittest.TestCase):

    def setUp(self):
        self.tree = BST(None)
        self.tree.AddKeyValue(10, 1)
        self.tree.AddKeyValue(8, 2)
        self.tree.AddKeyValue(12, 3)
        self.tree.AddKeyValue(5, 4)
        self.tree.AddKeyValue(3, 4)
        self.tree.AddKeyValue(1, 4)
        self.tree.AddKeyValue(6, 4)
        self.tree.AddKeyValue(16, 5)
        self.tree.AddKeyValue(13, 6)
        self.tree.AddKeyValue(18, 7)
        self.tree.AddKeyValue(9, 8)
        self.tree.AddKeyValue(11, 9)

    def test_deep_all_nodes_in_order(self):
        all_nodes = self.tree.DeepAllNodes(0)
        self.assertIsInstance(all_nodes, tuple)
        self.assertIsInstance(all_nodes[0], BSTNode)
        all_nodes_keys = [node.NodeKey for node in all_nodes]
        self.assertEqual(all_nodes_keys, sorted(all_nodes_keys))

    def test_deep_all_nodes_post_order(self):
        all_nodes = self.tree.DeepAllNodes(1)
        self.assertIsInstance(all_nodes, tuple)
        self.assertIsInstance(all_nodes[0], BSTNode)
        self.assertEqual(all_nodes[-1].NodeKey, self.tree.Root.NodeKey)

    def test_deep_all_nodes_pre_order(self):
        all_nodes = self.tree.DeepAllNodes(2)
        self.assertIsInstance(all_nodes, tuple)
        self.assertIsInstance(all_nodes[0], BSTNode)
        self.assertEqual(all_nodes[0].NodeKey, self.tree.Root.NodeKey)


if __name__ == '__main__':
    unittest.main()
