import unittest

from heap_array import Heap


class TestHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.heap = Heap()

    def test_make_empty_heap(self):
        array = []
        self.assertEqual(self.heap.HeapArray, array)
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.HeapArray, [None] * 7)
        self.assertEqual(self.heap.size, len(array))

    def test_make_full_heap(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.heap.HeapArray, [])
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.HeapArray, [7, 4, 6, 1, 3, 2, 5])
        self.assertEqual(self.heap.size, len(array))

    def test_make_not_full_heap(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(self.heap.HeapArray, [])
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.HeapArray, [5, 4, 2, 1, 3, None, None])
        self.assertEqual(self.heap.size, len(array))

    def test_add(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(self.heap.HeapArray, [])
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.HeapArray, [5, 4, 2, 1, 3, None, None])
        self.assertTrue(self.heap.Add(100))
        self.assertEqual(self.heap.HeapArray, [100, 4, 5, 1, 3, 2, None])
        self.assertEqual(self.heap.size, len(array) + 1)
        self.assertTrue(self.heap.Add(0))
        self.assertEqual(self.heap.HeapArray, [100, 4, 5, 1, 3, 2, 0])
        self.assertEqual(self.heap.size, len(array) + 2)
        self.assertFalse(self.heap.Add(99))  # проверка, если куча заполнена
        self.assertEqual(self.heap.HeapArray, [100, 4, 5, 1, 3, 2, 0])
        self.assertEqual(self.heap.size, len(array) + 2)

    def test_get_max(self):
        array = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.heap.HeapArray, [])
        self.heap.MakeHeap(array, 2)
        self.assertEqual(self.heap.HeapArray, [7, 4, 6, 1, 3, 2, 5])
        self.assertEqual(self.heap.size, len(array))
        self.assertEqual(self.heap.GetMax(), 7)
        self.assertEqual(self.heap.HeapArray, [6, 4, 5, 1, 3, 2, None])
        self.assertEqual(self.heap.size, len(array) - 1)
        self.assertEqual(self.heap.GetMax(), 6)
        self.assertEqual(self.heap.HeapArray, [5, 4, 2, 1, 3, None, None])
        self.assertEqual(self.heap.size, len(array) - 2)
        self.assertEqual(self.heap.GetMax(), 5)
        self.assertEqual(self.heap.HeapArray, [4, 3, 2, 1, None, None, None])
        self.assertEqual(self.heap.size, len(array) - 3)
        self.assertEqual(self.heap.GetMax(), 4)
        self.assertEqual(
            self.heap.HeapArray, [3, 1, 2, None, None, None, None])
        self.assertEqual(self.heap.size, len(array) - 4)
        self.assertEqual(self.heap.GetMax(), 3)
        self.assertEqual(
            self.heap.HeapArray, [2, 1, None, None, None, None, None])
        self.assertEqual(self.heap.size, len(array) - 5)
        self.assertEqual(self.heap.GetMax(), 2)
        self.assertEqual(
            self.heap.HeapArray, [1, None, None, None, None, None, None])
        self.assertEqual(self.heap.size, len(array) - 6)
        self.assertEqual(self.heap.GetMax(), 1)
        self.assertEqual(self.heap.HeapArray, [None] * 7)
        self.assertEqual(self.heap.size, 0)
        self.assertEqual(self.heap.GetMax(), -1)  # если массив пуст


if __name__ == '__main__':
    unittest.main()
