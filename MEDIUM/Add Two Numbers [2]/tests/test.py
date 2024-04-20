import unittest
from typing import Optional
from ..scripts.code import *

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_add_two_numbers_example_1(self):
        l1 = ListNode([2, 4, 3])
        l2 = ListNode([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = ListNode([7, 0, 8])
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertIsNone(result.next.next.next)

    def test_add_two_numbers_example_2(self):
        l1 = ListNode([0])
        l2 = ListNode([0])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = ListNode([0])
        self.assertEqual(result.val, expected.val)
        self.assertIsNone(result.next)

    def test_add_two_numbers_example_3(self):
        l1 = ListNode([9, 9, 9, 9, 9, 9, 9])
        l2 = ListNode([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        expected = ListNode([8, 9, 9, 9, 0, 0, 0, 1])
        self.assertEqual(result.val, expected.val)
        self.assertEqual(result.next.val, expected.next.val)
        self.assertEqual(result.next.next.val, expected.next.next.val)
        self.assertEqual(result.next.next.next.val, expected.next.next.next.val)
        self.assertEqual(result.next.next.next.next.val, expected.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.val, expected.next.next.next.next.next.val)
        self.assertEqual(result.next.next.next.next.next.next.val, expected.next.next.next.next.next.next.val)
        self.assertIsNone(result.next.next.next.next.next.next.next)

    def test_add_two_numbers_invalid_input(self):
        l1 = ListNode([1, 2, 3])
        l2 = ListNode([5, 6, 4])
        with self.assertRaises(AssertionError):
            self.solution.addTwoNumbers(l1, None)

if __name__ == "__main__":
    unittest.main()