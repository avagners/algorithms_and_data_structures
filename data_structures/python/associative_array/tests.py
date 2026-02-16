import random
import unittest
from string import ascii_letters

from NativeDictionary import NativeDictionary


class TestNativeDictEmptySlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_dict = NativeDictionary(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.key = ''.join(random.sample(ascii_letters, self.number))
        self.value = ''.join(random.sample(ascii_letters, self.number))
        self.empty_slots = [None] * self.size

    def test_check_native_dict(self):
        self.assertIsInstance(self.s_dict, NativeDictionary)
        self.assertEqual(len(self.s_dict.slots), self.size)
        self.assertEqual(len(self.s_dict.values), self.size)
        self.assertListEqual(self.s_dict.slots, self.empty_slots)
        self.assertListEqual(self.s_dict.values, self.empty_slots)
        for index in range(self.size):
            self.assertIsNone(self.s_dict.slots[index])
            self.assertIsNone(self.s_dict.values[index])

    def test_hash_fun_empty_slots(self):
        hash = self.s_dict.hash_fun(self.key)
        check_hash = sum([ord(sym) for sym in self.key]) % self.size
        self.assertEqual(hash, check_hash)

    def test_is_key_empty_slots(self):
        is_key = self.s_dict.is_key(self.key)
        self.assertFalse(is_key)

    def test_put_in_empty_slots(self):
        self.s_dict.put(self.key, self.value)
        self.assertIn(self.key, self.s_dict.slots)
        self.assertIn(self.value, self.s_dict.values)

    def test_get_in_empty_slots(self):
        value = self.s_dict.get(self.key)
        self.assertIsNone(value)


class TestNativeDictFullSlots(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_dict = NativeDictionary(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.new_key = ''.join(random.sample(ascii_letters, self.number))
        self.new_value = ''.join(random.sample(ascii_letters, self.number))
        self.full_keys = []
        self.full_values = []
        for _ in range(self.size):
            number = random.randint(3, len(ascii_letters))
            key = ''.join(random.sample(ascii_letters, number))
            value = ''.join(random.sample(ascii_letters, number))
            self.full_keys.append(key)
            self.full_values.append(value)
        for index in range(self.size):
            self.s_dict.slots[index] = self.full_keys[index]
            self.s_dict.values[index] = self.full_values[index]

    def test_check_native_dict_full_slots(self):
        self.assertIsInstance(self.s_dict, NativeDictionary)
        self.assertEqual(len(self.s_dict.slots), self.size)
        self.assertEqual(len(self.s_dict.values), self.size)
        self.assertListEqual(self.s_dict.slots, self.full_keys)
        self.assertListEqual(self.s_dict.values, self.full_values)
        for index in range(self.size):
            self.assertIsNotNone(self.s_dict.slots[index])
            self.assertIsNotNone(self.s_dict.values[index])

    def test_hash_fun_full_slots(self):
        hash = self.s_dict.hash_fun(self.new_key)
        check_hash = sum([ord(sym) for sym in self.new_key]) % self.size
        self.assertEqual(hash, check_hash)

    def test_is_key_full_slots(self):
        for key in self.full_keys:
            is_key = self.s_dict.is_key(key)
            self.assertTrue(is_key)
        is_new_key = self.s_dict.is_key(self.new_key)
        self.assertFalse(is_new_key)

    def test_put_new_key_in_full_slots(self):
        self.s_dict.put(self.new_key, self.new_value)
        self.assertNotIn(self.new_key, self.s_dict.slots)
        self.assertNotIn(self.new_value, self.s_dict.values)

    def test_put_new_value_in_full_slots(self):
        key_from_dict = random.choice(self.s_dict.slots)
        self.s_dict.put(key_from_dict, self.new_value)
        self.assertIn(key_from_dict, self.s_dict.slots)
        self.assertIn(self.new_value, self.s_dict.values)

    def test_get_in_full_slots(self):
        for index, key in enumerate(self.s_dict.slots):
            value = self.s_dict.get(key)
            self.assertIsNotNone(value)
            self.assertIsInstance(value, str)
            self.assertIn(value, self.full_values)
            self.assertEqual(self.full_values.index(value), index)


class TestNativeDictOneItem(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_dict = NativeDictionary(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.key = ''.join(random.sample(ascii_letters, self.number))
        self.value = ''.join(random.sample(ascii_letters, self.number))
        self.new_key = ''.join(random.sample(ascii_letters, self.number))
        self.new_value = ''.join(random.sample(ascii_letters, self.number))
        self.hash = self.s_dict.hash_fun(self.key)
        self.list_keys = [None] * self.size
        self.list_values = [None] * self.size
        self.list_keys[self.hash] = self.key
        self.list_values[self.hash] = self.value
        self.s_dict.put(self.key, self.value)

    def test_check_native_dict_one_item(self):
        self.assertIsInstance(self.s_dict, NativeDictionary)
        self.assertEqual(len(self.s_dict.slots), self.size)
        self.assertEqual(len(self.s_dict.values), self.size)
        self.assertListEqual(self.s_dict.slots, self.list_keys)
        self.assertListEqual(self.s_dict.values, self.list_values)
        self.assertIsNotNone(self.s_dict.slots[self.hash])
        self.assertIsNotNone(self.s_dict.values[self.hash])

    def test_hash_fun_one_item(self):
        hash = self.s_dict.hash_fun(self.new_key)
        check_hash = sum([ord(sym) for sym in self.new_key]) % self.size
        self.assertEqual(hash, check_hash)

    def test_is_key_one_item(self):
        is_key = self.s_dict.is_key(self.key)
        self.assertTrue(is_key)
        is_new_key = self.s_dict.is_key(self.new_key)
        self.assertFalse(is_new_key)

    def test_put_new_key_in_one_item(self):
        self.assertNotIn(self.new_key, self.s_dict.slots)
        self.s_dict.put(self.new_key, self.new_value)
        self.assertIn(self.new_key, self.s_dict.slots)
        self.assertIn(self.new_value, self.s_dict.values)
        self.assertEqual(
            self.s_dict.slots.index(self.new_key),
            self.s_dict.values.index(self.new_value)
        )

    def test_put_new_value_in_one_item(self):
        self.assertIn(self.key, self.s_dict.slots)
        self.assertNotIn(self.new_value, self.s_dict.values)
        self.s_dict.put(self.key, self.new_value)
        self.assertIn(self.new_value, self.s_dict.values)

    def test_get_in_one_item(self):
        value = self.s_dict.get(self.key)
        self.assertIsNotNone(value)
        self.assertIsInstance(value, str)
        self.assertIn(value, self.s_dict.values)
        self.assertEqual(value, self.value)


class TestNativeDictLastSlot(unittest.TestCase):

    def setUp(self):
        self.size = 17
        self.s_dict = NativeDictionary(self.size)
        self.number = random.randint(3, len(ascii_letters))
        self.new_key = ''.join(random.sample(ascii_letters, self.number))
        self.new_value = ''.join(random.sample(ascii_letters, self.number))
        self.list_keys = []
        self.list_values = []
        for index in range(self.size):
            number = random.randint(3, len(ascii_letters))
            key = ''.join(random.sample(ascii_letters, number))
            value = ''.join(random.sample(ascii_letters, number))
            self.list_keys.append(key)
            self.list_values.append(value)
        self.none_index = random.randrange(self.size)
        self.list_keys.pop(self.none_index)
        self.list_values.pop(self.none_index)
        for index in range(len(self.list_keys)):
            self.s_dict.put(self.list_keys[index], self.list_values[index])

    def test_check_native_dict_last_slot(self):
        self.assertIsInstance(self.s_dict, NativeDictionary)
        self.assertEqual(len(self.s_dict.slots), self.size)
        self.assertEqual(len(self.s_dict.values), self.size)
        self.assertIn(None, self.s_dict.slots)
        self.assertIn(None, self.s_dict.values)

    def test_hash_fun_last_slot(self):
        hash = self.s_dict.hash_fun(self.new_key)
        check_hash = sum([ord(sym) for sym in self.new_key]) % self.size
        self.assertEqual(hash, check_hash)

    def test_is_key_last_slot(self):
        is_key = self.s_dict.is_key(random.choice(self.s_dict.slots))
        self.assertTrue(is_key)
        is_new_key = self.s_dict.is_key(self.new_key)
        self.assertFalse(is_new_key)

    def test_put_new_key_in_last_slot(self):
        self.assertIn(None, self.s_dict.slots)
        self.assertIn(None, self.s_dict.values)
        self.assertNotIn(self.new_key, self.s_dict.slots)
        self.s_dict.put(self.new_key, self.new_value)
        self.assertIn(self.new_key, self.s_dict.slots)
        self.assertIn(self.new_value, self.s_dict.values)
        self.assertEqual(
            self.s_dict.slots.index(self.new_key),
            self.s_dict.values.index(self.new_value)
        )
        for index in range(self.size):
            self.assertIsNotNone(self.s_dict.slots[index])
            self.assertIsNotNone(self.s_dict.values[index])
            self.assertIsInstance(self.s_dict.slots[index], str)
            self.assertIsInstance(self.s_dict.values[index], str)

    def test_put_new_value_in_last_slot(self):
        key = random.choice(self.list_keys)
        self.assertIn(None, self.s_dict.slots)
        self.assertIn(None, self.s_dict.values)
        self.assertIn(key, self.s_dict.slots)
        self.assertNotIn(self.new_value, self.s_dict.values)
        self.s_dict.put(key, self.new_value)
        self.assertIn(self.new_value, self.s_dict.values)
        self.assertIn(None, self.s_dict.slots)

    def test_get_in_last_slot(self):
        key = random.choice(self.list_keys)
        value = self.s_dict.get(key)
        self.assertIsNotNone(value)
        self.assertIsInstance(value, str)
        self.assertIn(value, self.s_dict.values)
        new_value = self.s_dict.get(self.new_key)
        self.assertNotIn(self.new_key, self.s_dict.slots)
        self.assertIsNone(new_value)


if __name__ == '__main__':
    unittest.main()
