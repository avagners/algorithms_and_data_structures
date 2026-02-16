class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey: int = key  # ключ узла
        self.NodeValue: int = val  # значение в узле
        self.Parent: BSTNode = parent  # родитель или None для корня
        self.LeftChild: BSTNode = None  # левый потомок
        self.RightChild: BSTNode = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node: BSTNode = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey: bool = False  # True если узел найден
        self.ToLeft: bool = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node: BSTNode):
        self.Root = node  # корень дерева, или None
        self.__size = 0 if not node else 1

    def __find_node(self, search_result: BSTFind, key: int) -> BSTNode:
        node = search_result.Node
        if key == node.NodeKey:
            search_result.NodeHasKey = True
            return search_result
        elif key < node.NodeKey and node.LeftChild:
            search_result.Node = node.LeftChild
            return self.__find_node(search_result, key)
        elif key > node.NodeKey and node.RightChild:
            search_result.Node = node.RightChild
            return self.__find_node(search_result, key)
        search_result.ToLeft = key < node.NodeKey
        return search_result

    def FindNodeByKey(self, key: int) -> BSTFind:
        if not self.Root:
            return BSTFind()
        search_result = BSTFind()
        search_result.Node = self.Root
        return self.__find_node(search_result, key)

    def AddKeyValue(self, key: int, val: int):
        search_result = self.FindNodeByKey(key)
        if search_result.NodeHasKey:
            return False  # если ключ уже есть
        new_node = BSTNode(key, val, parent=search_result.Node)
        if not search_result.Node:
            self.Root = BSTNode(key, val, parent=None)
        elif search_result.ToLeft:
            search_result.Node.LeftChild = new_node
        else:
            search_result.Node.RightChild = new_node
        self.__size += 1
        return True

    def FinMinMax(self, FromNode: BSTNode, FindMax: bool) -> BSTNode:
        if not self.Root:
            return None
        if FindMax and FromNode.RightChild:
            return self.FinMinMax(FromNode.RightChild, FindMax)
        if not FindMax and FromNode.LeftChild:
            return self.FinMinMax(FromNode.LeftChild, FindMax)
        return FromNode

    def __insert_left_or_right_node(self, node_delete: BSTNode,
                                    node_successor: BSTNode):
        # проверяем какой узел удаляем - правый или левый
        is_left = node_delete.NodeKey < node_delete.Parent.NodeKey
        if is_left:
            node_delete.Parent.LeftChild = node_successor
        else:
            node_delete.Parent.RightChild = node_successor

    def __insert_node(self, node_delete: BSTNode, node_successor: BSTNode):
        if node_delete == self.Root:
            self.Root = node_successor
            self.Root.Parent = None
        else:
            self.__insert_left_or_right_node(node_delete, node_successor)
            # перемещаем преемника на место удаленного узла
            node_successor.Parent = node_delete.Parent
        node_successor.LeftChild = node_delete.LeftChild
        node_successor.RightChild = node_delete.RightChild

    def is_leaf(self, node: BSTNode) -> bool:
        return not node.LeftChild and not node.RightChild

    def DeleteNodeByKey(self, key: int) -> bool:
        # удаляем узел по ключу
        bst_find = self.FindNodeByKey(key)
        node_delete = bst_find.Node
        if not bst_find.NodeHasKey:
            return False
        # если в дереве только один узел
        if not node_delete.Parent and self.is_leaf(node_delete):
            self.Root = None
            self.__size -= 1
            return True
        # если удаляем последний узел дерева
        if self.is_leaf(node_delete):
            self.__insert_left_or_right_node(node_delete, None)
            self.__size -= 1
            return True
        # находим преемника
        node_successor = self.FinMinMax(node_delete.RightChild, False)
        successor_is_leaf = self.is_leaf(node_successor)
        # если у преемника нет потомков
        # и родитель является удаляемым узлом
        if node_successor.Parent == node_delete and successor_is_leaf:
            node_successor.Parent.RightChild = None
            node_delete.LeftChild.Parent = node_successor
            self.__insert_node(node_delete, node_successor)
        # если у преемника есть правый потомок
        # и родитель является удаляемым узлом
        elif node_successor.Parent == node_delete and not successor_is_leaf:
            node_successor.Parent.RightChild = node_successor.RightChild
            node_delete.LeftChild.Parent = node_successor
            self.__insert_node(node_delete, node_successor)
        # если у преемника нет потомков, то удаляем
        # у родителя преемника левый потомок
        elif successor_is_leaf:
            node_successor.Parent.LeftChild = None
            node_delete.RightChild.Parent = node_successor
            node_delete.LeftChild.Parent = node_successor
            self.__insert_node(node_delete, node_successor)
        # если у преемника есть только правый потомок, то
        # на место преемника ставим этот потомок
        elif not successor_is_leaf:
            node_delete.LeftChild.Parent = node_successor
            node_delete.RightChild.Parent = node_successor
            node_successor.Parent.LeftChild = node_successor.RightChild
            node_successor.RightChild.Parent = node_successor.Parent
            self.__insert_node(node_delete, node_successor)
        self.__size -= 1
        return True

    def Count(self) -> int:
        return len(self.GetAllNodes())  # количество узлов в дереве

    def __get_all_nodes(self, node: BSTNode) -> list:
        '''
        Приватный метод рекурсивно проходит по дереву и
        возвращает список всех узлов.
        '''
        nodes = []
        nodes.append(node)
        if node.LeftChild:
            nodes += self.__get_all_nodes(node.LeftChild)
        if node.RightChild:
            nodes += self.__get_all_nodes(node.RightChild)
        return nodes

    def GetAllNodes(self) -> list:
        if not self.Root:
            return []
        return self.__get_all_nodes(self.Root)

    def WideAllNodes(self) -> tuple:
        if not self.Root:
            return ()
        all_nodes = []
        nodes_in_level = [self.Root]  # начинаем с корня
        while nodes_in_level:
            node = nodes_in_level.pop(0)
            all_nodes.append(node)
            if node.LeftChild:
                nodes_in_level.append(node.LeftChild)
            if node.RightChild:
                nodes_in_level.append(node.RightChild)
        return tuple(all_nodes)

    def DeepAllNodes(self, type_order: int) -> tuple:
        if not self.Root:
            return ()
        all_nodes = []
        if type_order == 0:
            self.__in_order(self.Root, all_nodes)
        elif type_order == 1:
            self.__post_order(self.Root, all_nodes)
        elif type_order == 2:
            self.__pre_order(self.Root, all_nodes)
        return tuple(all_nodes)

    def __in_order(self, node, all_nodes):
        if node:
            self.__in_order(node.LeftChild, all_nodes)
            all_nodes.append(node)
            self.__in_order(node.RightChild, all_nodes)

    def __post_order(self, node, all_nodes):
        if node:
            self.__post_order(node.LeftChild, all_nodes)
            self.__post_order(node.RightChild, all_nodes)
            all_nodes.append(node)

    def __pre_order(self, node, all_nodes):
        if node:
            all_nodes.append(node)
            self.__pre_order(node.LeftChild, all_nodes)
            self.__pre_order(node.RightChild, all_nodes)
