import unittest

from binary_search_tree_array import aBST


class TestABSTreeSize(unittest.TestCase):

    def test_tree_size(self):
        self.tree = aBST(2)
        self.assertEqual(len(self.tree.Tree), 7)
        self.tree2 = aBST(3)
        self.assertEqual(len(self.tree2.Tree), 15)
        self.tree3 = aBST(4)
        self.assertEqual(len(self.tree3.Tree), 31)


class TestABST(unittest.TestCase):

    def test_full_tree(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, 100]
        for index, key in enumerate(tree.Tree):
            self.assertEqual(tree.FindKeyIndex(key), index)

    def test_one_none_value(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, None]
        self.assertEqual(tree.FindKeyIndex(90), -6)

    def test_if_not_exists(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, 100]
        self.assertIsNone(tree.FindKeyIndex(1000))

    def test_empty_tree(self):
        tree = aBST(1)
        self.assertEqual(tree.FindKeyIndex(1000), 0)

    def test_add_key(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, None]
        self.assertEqual(tree.AddKey(90), 6)
        self.assertEqual(tree.Tree[6], 90)

    def test_add_key_in_empty_tree(self):
        tree = aBST(1)
        self.assertEqual(tree.AddKey(90), 0)
        self.assertEqual(tree.Tree[0], 90)

    def test_add_existing_key(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, 90]
        self.assertEqual(tree.AddKey(50), 0)
        self.assertEqual(tree.Tree[0], 50)
        self.assertEqual(tree.AddKey(90), 6)
        self.assertEqual(tree.Tree[6], 90)
        self.assertEqual(tree.AddKey(15), 3)
        self.assertEqual(tree.Tree[3], 15)

    def test_add_key_in_full_tree(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, 90]
        self.assertEqual(tree.AddKey(100), -1)
        self.assertNotIn(100, tree.Tree)

    def test_add_key_if_no_suitable_place(self):
        tree = aBST(2)
        tree.Tree = [50, 25, 75, 15, 35, 65, None]
        self.assertEqual(tree.AddKey(60), -1)
        self.assertNotIn(60, tree.Tree)
        self.assertEqual(tree.AddKey(1), -1)
        self.assertNotIn(1, tree.Tree)


if __name__ == '__main__':
    unittest.main()
