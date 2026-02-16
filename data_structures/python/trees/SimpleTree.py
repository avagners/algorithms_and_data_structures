from typing import List


class SimpleTreeNode:

    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов
        self.Level = None  # уровень узла в дереве


class SimpleTree:

    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        NewChild.Parent = ParentNode
        if ParentNode is None:
            self.Root = NewChild
        else:
            ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        '''
        Метод удаления узла вместе с дочерними узлами.
        '''
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def __get_all_nodes(self, node: SimpleTreeNode) -> List[SimpleTreeNode]:
        '''
        Приватный метод рекурсивно проходит по дереву и
        возвращает список всех узлов.
        '''
        nodes = []
        nodes.append(node)
        for child in node.Children:
            nodes += self.__get_all_nodes(child)
        return nodes

    def GetAllNodes(self) -> List[SimpleTreeNode]:
        if self.Root is None:
            return []
        return self.__get_all_nodes(self.Root)

    def FindNodesByValue(self, val: int) -> List[SimpleTreeNode]:
        return [node for node in self.GetAllNodes() if node.NodeValue == val]

    def MoveNode(self, OriginalNode, NewParent):
        '''
        Метод перемещения узла вместе с его поддеревом
        в качестве дочернего для узла NewParent.
        '''
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self) -> int:
        return len(self.GetAllNodes())

    def LeafCount(self) -> int:
        return len([node for node in self.GetAllNodes() if not node.Children])

    def __set_level_nodes(self, node: SimpleTreeNode) -> None:
        '''
        Приватный метод рекурсивно проходит по дереву
        и устанавливает уровень узла в дереве.
        '''
        if node == self.Root:
            node.Level = 0
        for child in node.Children:
            child.Level = child.Parent.Level + 1
            self.__set_level_nodes(child)

    def SetLevelNodes(self):
        self.__set_level_nodes(self.Root)

    def __nodes_to_remove_edge(self, node: SimpleTreeNode, nodes_remove_edge: list):
        count = 1
        for child in node.Children:
            count += self.__nodes_to_remove_edge(child, nodes_remove_edge)
        if count % 2 == 0 and node.Parent:
            nodes_remove_edge.append(node.Parent)
            nodes_remove_edge.append(node)
            count = 0
        return count

    def EvenTrees(self) -> List[SimpleTreeNode]:
        '''
        Метод находит узлы, между которыми нужно
        удалить связь для создания леса из чётных деревьев.
        '''
        if not self.Root:
            return []
        roots_even_trees = []
        self.__nodes_to_remove_edge(self.Root, roots_even_trees)
        return roots_even_trees
