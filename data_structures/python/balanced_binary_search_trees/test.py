import unittest

from balanced_bst import BalancedBST, BSTNode


class TestGenerateBBSTArray(unittest.TestCase):

    def test_generate_tree_empty(self):
        array = []
        tree = BalancedBST()
        tree.GenerateTree(array)
        self.assertIsNone(tree.Root)

    def test_generate_tree_one_level(self):
        array = [3, 2, 1]
        tree = BalancedBST()
        tree.GenerateTree(array)
        self.assertIsInstance(tree.Root, BSTNode)
        self.assertIsInstance(tree.Root.LeftChild, BSTNode)
        self.assertIsInstance(tree.Root.RightChild, BSTNode)
        self.assertEqual(tree.Root.NodeKey, 2)
        self.assertEqual(tree.Root.Level, 0)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 1)
        self.assertEqual(tree.Root.RightChild.NodeKey, 3)
        self.assertEqual(tree.Root.LeftChild.Level, 1)
        self.assertEqual(tree.Root.RightChild.Level, 1)
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(tree.Root.LeftChild.Parent, tree.Root)
        self.assertEqual(tree.Root.RightChild.Parent, tree.Root)
        self.assertIsNone(tree.Root.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild)
        self.assertIsNone(tree.Root.RightChild.LeftChild)
        self.assertIsNone(tree.Root.RightChild.RightChild)
        self.assertGreaterEqual(
            tree.Root.RightChild.NodeKey,
            tree.Root.LeftChild.NodeKey
        )

    def test_generate_tree_two_level(self):
        array = [3, 2, 1, 5, 4, 7, 6]
        tree = BalancedBST()
        tree.GenerateTree(array)
        self.assertIsInstance(tree.Root, BSTNode)
        self.assertIsInstance(tree.Root.LeftChild, BSTNode)
        self.assertIsInstance(tree.Root.RightChild, BSTNode)
        self.assertEqual(tree.Root.NodeKey, 4)
        self.assertEqual(tree.Root.Level, 0)
        self.assertEqual(tree.Root.LeftChild.NodeKey, 2)
        self.assertEqual(tree.Root.RightChild.NodeKey, 6)
        self.assertEqual(tree.Root.LeftChild.Level, 1)
        self.assertEqual(tree.Root.RightChild.Level, 1)
        self.assertIsNone(tree.Root.Parent)
        self.assertEqual(tree.Root.LeftChild.Parent, tree.Root)
        self.assertEqual(tree.Root.RightChild.Parent, tree.Root)
        self.assertIsInstance(tree.Root.LeftChild.LeftChild, BSTNode)
        self.assertIsInstance(tree.Root.LeftChild.RightChild, BSTNode)
        self.assertIsInstance(tree.Root.RightChild.LeftChild, BSTNode)
        self.assertIsInstance(tree.Root.RightChild.RightChild, BSTNode)
        self.assertGreaterEqual(
            tree.Root.RightChild.NodeKey, tree.Root.LeftChild.NodeKey
        )
        self.assertGreaterEqual(
            tree.Root.RightChild.RightChild.NodeKey,
            tree.Root.RightChild.LeftChild.NodeKey
        )
        self.assertGreaterEqual(
            tree.Root.LeftChild.RightChild.NodeKey,
            tree.Root.LeftChild.LeftChild.NodeKey
        )
        self.assertIsNone(tree.Root.LeftChild.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.LeftChild.RightChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild.LeftChild)
        self.assertIsNone(tree.Root.LeftChild.RightChild.RightChild)
        self.assertIsNone(tree.Root.RightChild.LeftChild.LeftChild)
        self.assertIsNone(tree.Root.RightChild.LeftChild.RightChild)
        self.assertIsNone(tree.Root.RightChild.RightChild.LeftChild)
        self.assertIsNone(tree.Root.RightChild.RightChild.RightChild)

    def test_is_balanced(self):
        array = [3, 2, 1, 5, 4, 7, 6]
        tree = BalancedBST()
        tree.GenerateTree(array)
        self.assertTrue(tree.IsBalanced(tree.Root))
        tree.Root.RightChild.RightChild = None
        tree.Root.RightChild.LeftChild = None
        self.assertTrue(tree.IsBalanced(tree.Root))
        tree.Root.RightChild = None
        self.assertFalse(tree.IsBalanced(tree.Root))

    def test_is_balanced_empty_tree(self):
        tree = BalancedBST()
        self.assertTrue(tree.IsBalanced(tree.Root))


if __name__ == '__main__':
    unittest.main()
