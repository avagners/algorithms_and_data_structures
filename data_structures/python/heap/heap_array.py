class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи
        self.size = 0  # кол-во ключей

    def MakeHeap(self, a: list, depth: int):
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        heap_size = 2**(depth + 1) - 1
        self.HeapArray = [None] * heap_size
        [self.Add(i) for i in a]

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        if not self.HeapArray[0]:
            return -1  # если куча пуста
        root_key = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self.size-1]
        self.HeapArray[self.size-1] = None
        self.size -= 1
        self.__take_right_places(self.HeapArray, 0, push_up=False)
        return root_key

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        if None not in self.HeapArray:
            return False  # если куча вся заполнена
        index = self.HeapArray.index(None)
        self.HeapArray[index] = key
        self.size += 1
        self.__take_right_places(self.HeapArray, index, push_up=True)
        return True

    def __push_up(self, array, index):
        if index == 0:
            return
        parent_index = (index - 1) // 2
        key = array[index]
        parent = array[parent_index]
        if key < parent:
            return
        if key > parent:
            array[index], array[parent_index] = array[parent_index], array[index]
            self.__push_up(array, parent_index)

    def __push_down(self, array, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        if right_child_index > len(self.HeapArray):
            return
        left_child = array[left_child_index]
        right_child = array[right_child_index]
        max_index = None
        if not left_child and not right_child:
            return
        if left_child and not right_child:
            max_index = left_child_index
        elif not left_child and right_child:
            max_index = right_child_index
        elif left_child and right_child:
            max_index = (right_child_index if
                         right_child > left_child else
                         left_child_index)
        key = array[index]
        if key > array[max_index]:
            return
        if key < array[max_index]:
            array[index], array[max_index] = array[max_index], array[index]
            self.__push_down(array, max_index)

    def __take_right_places(self, array, index, push_up):
        if push_up:
            self.__push_up(array, index)
            return
        self.__push_down(array, index)
