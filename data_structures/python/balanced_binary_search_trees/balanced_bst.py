class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey: int = key  # ключ узла
        self.Parent: BSTNode = parent  # родитель или None для корня
        self.LeftChild: BSTNode = None  # левый потомок
        self.RightChild: BSTNode = None  # правый потомок
        self.Level: int = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def GenerateTree(self, a: list):
        # создаём дерево с нуля из неотсортированного массива a
        if not a:
            return
        sorted_array = sorted(a)
        self.Root = self.__array_to_bbst(
            sorted_array, node_parent=None, level=0
        )

    def __array_to_bbst(self, sorted_array: list,
                        node_parent: BSTNode, level: int) -> BSTNode:
        middle_index = len(sorted_array) // 2
        node = BSTNode(sorted_array[middle_index], node_parent)
        node.Level = level
        if len(sorted_array) > 1:
            left_subtree = sorted_array[:middle_index]
            node.LeftChild = self.__array_to_bbst(
                left_subtree, node, level + 1
            )
            right_subtree = sorted_array[middle_index+1:]
            node.RightChild = self.__array_to_bbst(
                right_subtree, node, level + 1
            )
        return node

    def IsBalanced(self, root_node: BSTNode):
        if root_node is None:
            return True
        return self.__get_info_subtree(root_node)[0]

    def __get_info_subtree(self, sub_root: BSTNode):
        if sub_root is None:
            return True, 0
        left_balanced, left_level = self.__get_info_subtree(sub_root.LeftChild)
        right_balanced, right_level = self.__get_info_subtree(sub_root.RightChild)
        is_balanced = (left_balanced and right_balanced and
                       abs(left_level - right_level) <= 1)
        return is_balanced, max(left_level, right_level) + 1
