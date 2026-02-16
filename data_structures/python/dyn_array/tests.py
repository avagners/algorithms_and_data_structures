import unittest
import random

from DynArray import DynArray


class TestOneItemDynArray(unittest.TestCase):

    def setUp(self):
        self.d_array = DynArray()
        self.d_array.append(1)
        self.len = self.d_array.__len__()
        self.capacity = self.d_array.capacity
        self.min_capacity = 16

    def test_one_item_check_d_array(self):
        self.assertEqual(self.d_array.__len__(), 1)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_one_item_insert(self):
        new_item = random.randint(0, 100)
        self.d_array.insert(0, new_item)
        self.assertEqual(self.d_array.__len__(), self.len + 1)
        self.assertEqual(self.d_array[0], new_item)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_one_item_delete(self):
        self.d_array.delete(0)
        self.assertEqual(self.d_array.__len__(), self.len - 1)
        with self.assertRaises(IndexError):
            self.d_array[0]
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_one_item_raises(self):
        new_item = random.randint(0, 100)
        with self.assertRaises(IndexError):
            self.d_array.insert(-1, new_item)
        with self.assertRaises(IndexError):
            self.d_array.insert(self.len + 1, new_item)
        with self.assertRaises(IndexError):
            self.d_array.delete(-1)
        with self.assertRaises(IndexError):
            self.d_array.delete(self.len)


class TestEmptyDynArray(unittest.TestCase):

    def setUp(self):
        self.d_array = DynArray()
        self.len = self.d_array.__len__()
        self.capacity = self.d_array.capacity
        self.min_capacity = 16

    def test_empty_check_d_array(self):
        self.assertEqual(self.d_array.__len__(), 0)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_empty_insert(self):
        new_item = random.randint(0, 100)
        self.d_array.insert(0, new_item)
        self.assertEqual(self.d_array.__len__(), self.len + 1)
        self.assertEqual(self.d_array[0], new_item)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_empty_delete(self):
        with self.assertRaises(IndexError):
            self.d_array.delete(0)
        self.assertEqual(self.d_array.__len__(), 0)
        self.assertEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_empty_raises(self):
        new_item = random.randint(0, 100)
        with self.assertRaises(IndexError):
            self.d_array.insert(-1, new_item)
        with self.assertRaises(IndexError):
            self.d_array.insert(self.len + 1, new_item)
        with self.assertRaises(IndexError):
            self.d_array.delete(-1)
        with self.assertRaises(IndexError):
            self.d_array.delete(self.len)


class TestManyItemsDynArray(unittest.TestCase):

    def setUp(self):
        self.d_array = DynArray()
        for i in range(16):
            self.d_array.append(i)
        self.len = self.d_array.__len__()
        self.capacity = self.d_array.capacity
        self.min_capacity = 16

    def test_many_items_check_d_array(self):
        self.assertEqual(self.d_array.__len__(), 16)
        self.assertEqual(self.d_array.capacity, self.min_capacity)

    def test_many_items_insert_first_place(self):
        new_item = random.randint(0, 100)
        self.d_array.insert(0, new_item)
        self.assertEqual(self.d_array.__len__(), self.len + 1)
        self.assertEqual(self.d_array[0], new_item)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.capacity * 2)

    def test_many_items_insert_last_place(self):
        new_item = random.randint(0, 100)
        self.d_array.insert(self.len, new_item)
        self.assertEqual(self.d_array.__len__(), self.len + 1)
        self.assertEqual(self.d_array[self.len], new_item)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.capacity * 2)

    def test_many_items_insert_middle_place(self):
        new_item = random.randint(0, 100)
        self.d_array.insert(1, new_item)
        self.assertEqual(self.d_array.__len__(), self.len + 1)
        self.assertEqual(self.d_array[1], new_item)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        self.assertEqual(self.d_array.capacity, self.capacity * 2)

    def test_many_items_delete_first_place(self):
        self.d_array.delete(0)
        self.assertEqual(self.d_array.__len__(), self.len - 1)
        self.assertEqual(self.d_array.capacity, self.capacity)

    def test_many_items_delete_last_place(self):
        self.d_array.delete(self.len - 1)
        self.assertEqual(self.d_array.__len__(), self.len - 1)
        self.assertEqual(self.d_array.capacity, self.capacity)

    def test_many_items_delete_middle_place(self):
        self.d_array.delete(1)
        self.assertEqual(self.d_array.__len__(), self.len - 1)
        self.assertEqual(self.d_array.capacity, self.capacity)

    def test_many_items_raises(self):
        new_item = random.randint(0, 100)
        with self.assertRaises(IndexError):
            self.d_array.insert(-1, new_item)
        with self.assertRaises(IndexError):
            self.d_array.insert(self.len + 1, new_item)
        with self.assertRaises(IndexError):
            self.d_array.delete(-1)
        with self.assertRaises(IndexError):
            self.d_array.delete(self.len)

    def test_decrease_buffer_size(self):
        new_item = random.randint(0, 100)
        self.d_array.append(new_item)
        self.assertEqual(self.d_array.__len__(), self.len + 1)
        self.assertGreater(self.d_array.__len__(), self.capacity)
        self.assertNotEqual(self.d_array.capacity, self.capacity)
        new_capacity = self.capacity * 2
        self.assertEqual(self.d_array.capacity, new_capacity)
        self.d_array.delete(0)
        self.assertGreaterEqual(
            self.d_array.__len__(), self.d_array.capacity * 0.5
        )
        self.assertEqual(self.d_array.capacity, new_capacity)
        self.d_array.delete(0)
        self.assertLess(self.d_array.__len__(), new_capacity * 0.5)
        self.assertEqual(self.d_array.capacity, int(new_capacity / 1.5))

    def test_min_capacity(self):
        half_capacity_plus_one = int(self.d_array.capacity * 0.5) + 1
        for _ in range(half_capacity_plus_one):
            self.d_array.delete(0)
        self.assertEqual(
            self.d_array.__len__(), self.len - half_capacity_plus_one
        )
        self.assertEqual(self.d_array.capacity, self.min_capacity)


if __name__ == '__main__':
    unittest.main()
