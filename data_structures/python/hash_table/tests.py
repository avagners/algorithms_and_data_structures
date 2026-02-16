import random
import unittest
from string import ascii_letters

from HashTable import HashTable


class TestHashTableEmptySlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.step = 3
        self.s_hash = HashTable(self.size, self.step)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.empty_slots = [None for _ in range(self.size)]

    def test_check_hash_table_empty_slots(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.empty_slots)
        for index in range(self.size):
            self.assertIsNone(self.s_hash.slots[index])

    def test_hash_fun_empty_slots(self):
        hash = self.s_hash.hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)

    def test_seek_slot_empty_slots(self):
        slot = self.s_hash.seek_slot(self.string)
        self.assertIsInstance(slot, int)
        self.assertEqual(slot, self.s_hash.hash_fun(self.string))

    def test_put_in_empty_slots(self):
        index = self.s_hash.put(self.string)
        self.assertNotEqual(self.s_hash.slots, self.empty_slots)
        self.assertIsInstance(index, int)
        self.assertEqual(self.s_hash.slots[index], self.string)

    def test_find_in_empty_slots(self):
        index = self.s_hash.find(self.string)
        self.assertIsNone(index)


class TestHashTableFullSlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.step = 3
        self.s_hash = HashTable(self.size, self.step)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.full_slots = []
        for _ in range(self.size):
            number = random.randint(3, len(ascii_letters))
            string = ''.join(random.sample(ascii_letters, number))
            self.full_slots.append(string)
        for index, string in enumerate(self.full_slots):
            self.s_hash.slots[index] = string

    def test_check_hash_table_full_slots(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.full_slots)
        for index in range(self.size):
            self.assertIsNotNone(self.s_hash.slots[index])

    def test_hash_fun_full_slots(self):
        hash = self.s_hash.hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)

    def test_seek_slot_full_slots(self):
        slot = self.s_hash.seek_slot(self.string)
        self.assertIsNone(slot)
        self.assertNotEqual(slot, self.s_hash.hash_fun(self.string))

    def test_put_in_full_slots(self):
        index = self.s_hash.put(self.string)
        self.assertListEqual(self.s_hash.slots, self.full_slots)
        self.assertIsNone(index)

    def test_find_in_full_slots(self):
        string = random.choice(self.s_hash.slots)
        index = self.s_hash.find(string)
        self.assertIsInstance(index, int)
        self.assertIsNotNone(index)

    def test_find_return_none_in_full_slots(self):
        index = self.s_hash.find('string_not_exist')
        self.assertIsNone(index)


class TestHashTableOneItem(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.step = 3
        self.s_hash = HashTable(self.size, self.step)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.hash = self.s_hash.hash_fun(self.string)
        self.list_slots = [None for _ in range(self.size)]
        self.list_slots[self.hash] = self.string
        self.s_hash.put(self.string)

    def test_check_hash_table_one_item(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.list_slots)

    def test_hash_fun_one_item(self):
        hash = self.s_hash.hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)

    def test_seek_slot_same_string_one_item(self):
        slot = self.s_hash.seek_slot(self.string)
        self.assertIsNotNone(slot)
        self.assertIsInstance(slot, int)
        self.assertNotEqual(slot, self.s_hash.hash_fun(self.string))
        next_index = (
            self.s_hash.hash_fun(self.string) + self.step
        ) % self.size
        self.assertEqual(slot, next_index)

    def test_seek_slot_another_string_one_item(self):
        new_string = self.string + 'x'
        hash_new_string = self.s_hash.hash_fun(new_string)
        hash_old_string = self.s_hash.hash_fun(self.string)
        slot = self.s_hash.seek_slot(new_string)
        self.assertIsNotNone(slot)
        self.assertIsInstance(slot, int)
        self.assertNotEqual(hash_new_string, hash_old_string)
        self.assertEqual(slot, self.s_hash.hash_fun(new_string))

    def test_put_same_string_one_item(self):
        index = self.s_hash.put(self.string)
        self.list_slots[index] = self.string
        self.assertIsNotNone(index)
        self.assertIsInstance(index, int)
        next_index = (
            self.s_hash.hash_fun(self.string) + self.step
        ) % self.size
        self.assertEqual(index, next_index)
        self.assertListEqual(self.s_hash.slots, self.list_slots)

    def test_put_another_string_one_item(self):
        new_string = self.string + 'x'
        hash_new_string = self.s_hash.hash_fun(new_string)
        hash_old_string = self.s_hash.hash_fun(self.string)
        index = self.s_hash.put(new_string)
        self.assertNotEqual(hash_new_string, hash_old_string)
        self.list_slots[index] = new_string
        self.assertIsNotNone(index)
        self.assertIsInstance(index, int)
        self.assertEqual(index, hash_new_string)
        self.assertListEqual(self.s_hash.slots, self.list_slots)

    def test_find_in_one_item(self):
        index = self.s_hash.find(self.string)
        self.assertIsInstance(index, int)
        self.assertIsNotNone(index)
        self.assertEqual(index, self.hash)

    def test_find_return_none_in_one_item(self):
        index = self.s_hash.find('string_not_exist')
        self.assertIsNone(index)


class TestHashTableOneNoneItem(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.step = 3
        self.s_hash = HashTable(self.size, self.step)
        self.number = random.randint(3, len(ascii_letters))
        self.string = ''.join(random.sample(ascii_letters, self.number))
        self.list_slots = []
        for _ in range(self.size):
            number = random.randint(3, len(ascii_letters))
            string = ''.join(random.sample(ascii_letters, number))
            self.list_slots.append(string)
        for index, string in enumerate(self.list_slots):
            self.s_hash.slots[index] = string
        self.none_index = random.randrange(self.size)
        self.list_slots[self.none_index] = None
        self.s_hash.slots[self.none_index] = None

    def test_check_hash_table_one_none_item(self):
        self.assertIsInstance(self.s_hash, HashTable)
        self.assertEqual(len(self.s_hash.slots), self.size)
        self.assertListEqual(self.s_hash.slots, self.list_slots)

    def test_hash_fun_one_none_item(self):
        hash = self.s_hash.hash_fun(self.string)
        check_hash = sum([ord(sym) for sym in self.string]) % self.size
        self.assertEqual(hash, check_hash)

    def test_seek_slot_one_none_item(self):
        slot = self.s_hash.seek_slot(self.string)
        self.assertIsNotNone(slot)
        self.assertIsInstance(slot, int)
        self.assertEqual(slot, self.none_index)

    def test_put_one_none_item(self):
        index = self.s_hash.put(self.string)
        self.list_slots[index] = self.string
        self.assertIsNotNone(index)
        self.assertIsInstance(index, int)
        self.assertEqual(index, self.none_index)
        self.assertListEqual(self.s_hash.slots, self.list_slots)
        for index in range(self.size):
            self.assertIsNotNone(self.s_hash.slots[index])

    def test_find_in_one_none_item(self):
        item_in_slots = random.choice(self.s_hash.slots)
        index = self.s_hash.find(item_in_slots)
        self.assertIsNotNone(index)
        self.assertIsInstance(index, int)

    def test_find_return_none_in_one_none_item(self):
        index = self.s_hash.find('string_not_exist')
        self.assertIsNone(index)


if __name__ == '__main__':
    unittest.main()
