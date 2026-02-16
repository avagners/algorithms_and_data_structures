class aBST:

    def __init__(self, depth: int):
        tree_size: int = 2**(depth + 1) - 1
        self.Tree: list = [None] * tree_size  # массив ключей

    def __find_index(self, key: int, index: int) -> int:
        if index >= len(self.Tree):
            return None
        if not self.Tree[index]:
            return -index
        if self.Tree[index] == key:
            return index
        if self.Tree[index] > key:
            index_left_child = 2 * index + 1
            return self.__find_index(key, index_left_child)
        if self.Tree[index] < key:
            index_rignt_child = 2 * index + 2
            return self.__find_index(key, index_rignt_child)

    def FindKeyIndex(self, key: int) -> int:
        return self.__find_index(key, 0)

    def AddKey(self, key: int) -> int:
        """
        Метод возвращает индекс добавленного/существующего ключа
        или -1 если не удалось.
        """
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index < 0 or not self.Tree[0]:
            index *= -1
            self.Tree[index] = key
            return index
        return index
