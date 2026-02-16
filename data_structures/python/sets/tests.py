import random
import unittest
from datetime import datetime

from PowerSet import PowerSet


class TestPowerSet(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items_list1 = list(
            {random.randint(0, 1000000) for _ in range(
                20000
            )}
        )
        cls.items_list2 = list(
            {random.randint(1000001, 2000000) for _ in range(
                20000
            )}
        )
        cls.items_list3 = list(
            {random.randint(500000, 1500000) for _ in range(
                20000
            )}
        )

    def setUp(self):
        self.s_set = PowerSet()
        self.items_list = list(
            {random.randint(0, 1000000) for _ in range(
                20000
            )}
        )
        self.s_set.items = self.items_list
        self.len_set = len(self.s_set.items)

    def test_put_success(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        new_item = 1000001
        self.assertEqual(self.s_set.size(), self.len_set)
        self.assertNotIn(new_item, self.s_set.items)
        self.s_set.put(new_item)
        self.assertEqual(self.s_set.size(), self.len_set + 1)
        self.assertIn(new_item, self.s_set.items)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_put_fail(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        new_item = random.choice(self.s_set.items)
        self.assertEqual(self.s_set.size(), self.len_set)
        self.assertIn(new_item, self.s_set.items)
        self.s_set.put(new_item)
        self.assertEqual(self.s_set.size(), self.len_set)
        self.assertIn(new_item, self.s_set.items)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_remove_true(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        item = random.choice(self.s_set.items)
        self.assertEqual(self.s_set.size(), self.len_set)
        self.assertIn(item, self.s_set.items)
        result = self.s_set.remove(item)
        self.assertTrue(result)
        self.assertEqual(self.s_set.size(), self.len_set - 1)
        self.assertNotIn(item, self.s_set.items)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_remove_false(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        item = 1000001
        self.assertEqual(self.s_set.size(), self.len_set)
        self.assertNotIn(item, self.s_set.items)
        result = self.s_set.remove(item)
        self.assertFalse(result)
        self.assertEqual(self.s_set.size(), self.len_set)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_intersection_return_empty_set(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list2
        result = self.s_set.intersection(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertListEqual(result.items, [])
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_intersection_return_set(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list1
        result = self.s_set.intersection(set2)
        self.assertIsInstance(result, PowerSet)
        for item in result.items:
            self.assertIn(item, self.s_set.items)
            self.assertIn(item, set2.items)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_union_another_set2(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list2
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.size(), self.s_set.size() + set2.size())
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_union_set2_empty(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.size(), self.s_set.size() + set2.size())
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_union_set2(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list1
        result = self.s_set.union(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertLessEqual(result.size(), self.s_set.size() + set2.size())
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_difference_another_set2(self):
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list2
        start_time = datetime.now()
        result = self.s_set.difference(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertEqual(result.items, self.s_set.items)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_difference_identical_sets(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list
        self.assertListEqual(self.s_set.items, set2.items)
        result = self.s_set.difference(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertListEqual(result.items, [])
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_difference_sets(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list1
        result = self.s_set.difference(set2)
        self.assertIsInstance(result, PowerSet)
        self.assertLessEqual(result.size(), self.s_set.size())
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_issubset_identical_sets(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list
        result = self.s_set.issubset(set2)
        self.assertTrue(result)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_issubset_not_all_elements_sets(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list3
        result = self.s_set.issubset(set2)
        self.assertFalse(result)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')

    def test_issubset_self_set_issubset_set2(self):
        start_time = datetime.now()
        print(len(self.s_set.items))
        set2 = PowerSet()
        set2.items = self.items_list3
        self.s_set.items = self.items_list3[-3:]
        result = self.s_set.issubset(set2)
        self.assertFalse(result)
        print(len(self.s_set.items), datetime.now() - start_time, '\n')


if __name__ == '__main__':
    unittest.main()
