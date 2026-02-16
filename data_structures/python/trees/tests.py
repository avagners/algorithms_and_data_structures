import unittest

from SimpleTree import SimpleTree, SimpleTreeNode


class TestSimpleTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tree = SimpleTree(None)

    def setUp(self):
        self.node_root = SimpleTreeNode(6, None)
        self.new_node_2 = SimpleTreeNode(7, self.node_root)
        self.new_node_3 = SimpleTreeNode(8, self.node_root)
        self.new_node_4 = SimpleTreeNode(8, self.new_node_3)
        self.tree.AddChild(None, self.node_root)
        self.tree.AddChild(self.node_root, self.new_node_2)
        self.tree.AddChild(self.node_root, self.new_node_3)
        self.tree.AddChild(self.new_node_3, self.new_node_4)

    def test_add_node(self):
        self.assertEqual(self.tree.Count(), 4)
        new_node = SimpleTreeNode(10, self.node_root)
        self.tree.AddChild(self.node_root, new_node)
        self.assertEqual(self.tree.Count(), 5)
        self.assertIn(new_node, self.node_root.Children)
        self.assertEqual(new_node.Parent, self.node_root)

    def test_GetAllNodes(self):
        nodes = [self.node_root, self.new_node_2,
                 self.new_node_3, self.new_node_4]
        self.assertListEqual(self.tree.GetAllNodes(), nodes)

    def test_FindNodesByValue(self):
        find_nodes = self.tree.FindNodesByValue(8)
        self.assertEqual(find_nodes, [self.new_node_3, self.new_node_4])

    def test_Count(self):
        self.assertEqual(self.tree.Count(), 4)
        new_node = SimpleTreeNode(10, self.node_root)
        self.tree.AddChild(self.node_root, new_node)
        self.assertEqual(self.tree.Count(), 5)

    def test_LeafCount(self):
        self.assertEqual(self.tree.LeafCount(), 2)
        new_leaf = SimpleTreeNode(10, self.node_root)
        self.tree.AddChild(self.node_root, new_leaf)
        self.assertEqual(self.tree.LeafCount(), 3)
        new_leaf_2 = SimpleTreeNode(10, self.new_node_3)
        self.tree.AddChild(self.new_node_3, new_leaf_2)
        self.assertEqual(self.tree.LeafCount(), 4)
        new_not_leaf = SimpleTreeNode(11, self.new_node_2)
        self.tree.AddChild(self.new_node_2, new_not_leaf)
        self.assertEqual(self.tree.LeafCount(), 4)

    def test_DeleteNode(self):
        self.assertEqual(self.tree.Count(), 4)
        self.tree.DeleteNode(self.new_node_3)
        # проверяем кол-во узлов после удаления
        self.assertEqual(self.tree.Count(), 2)
        # проверяем отсутсвие удаленного узла в
        # списке Children родительского узла
        self.assertNotIn(self.new_node_3, self.tree.Root.Children)
        # проверяем отсутсвие удаленного узла и
        # всех его дочерних узлов в дереве
        self.assertNotIn(self.new_node_3, self.tree.GetAllNodes())
        self.assertNotIn(self.new_node_4, self.tree.GetAllNodes())

    def test_MoveNode(self):
        self.assertIn(self.new_node_3, self.tree.Root.Children)
        self.assertNotIn(self.new_node_3, self.new_node_3.Children)
        self.assertEqual(self.new_node_3.Children, [self.new_node_4])
        self.assertEqual(self.new_node_3.Parent, self.tree.Root)
        self.tree.MoveNode(
            OriginalNode=self.new_node_3,
            NewParent=self.new_node_2
        )
        self.assertNotIn(self.new_node_3, self.tree.Root.Children)
        self.assertIn(self.new_node_3, self.new_node_2.Children)
        self.assertEqual(self.new_node_3.Children, [self.new_node_4])
        self.assertEqual(self.new_node_3.Parent, self.new_node_2)

    def test_SetLevelNode(self):
        all_nodes = self.tree.GetAllNodes()
        for node in all_nodes:
            self.assertEqual(node.Level, None)
        # устанавливаем уровни всех узлов дерева
        self.tree.SetLevelNodes()
        for node in all_nodes:
            self.assertNotEqual(node.Level, None)
        self.assertEqual(self.tree.Root.Level, 0)
        for node in self.tree.Root.Children:
            self.assertEqual(node.Level, 1)
        self.assertEqual(self.new_node_4.Level, 2)

    def test_even_trees(self):
        node_5 = SimpleTreeNode(9, None)
        node_6 = SimpleTreeNode(10, None)
        node_7 = SimpleTreeNode(11, None)
        node_8 = SimpleTreeNode(12, None)
        node_9 = SimpleTreeNode(13, None)
        node_10 = SimpleTreeNode(14, None)
        self.tree.AddChild(self.new_node_2, node_5)
        self.tree.AddChild(self.new_node_2, node_6)
        self.tree.AddChild(self.new_node_4, node_7)
        self.tree.AddChild(self.new_node_4, node_8)
        self.tree.AddChild(self.new_node_4, node_9)
        self.tree.AddChild(self.new_node_3, node_10)
        self.assertListEqual(
            self.tree.EvenTrees(),
            [self.new_node_3, self.new_node_4, self.node_root, self.new_node_3]
        )


if __name__ == '__main__':
    unittest.main()
