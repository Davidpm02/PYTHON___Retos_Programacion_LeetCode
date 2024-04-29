import unittest
from ..scripts.code import *

class TestMergeTwoLists(unittest.TestCase):

    def test_both_lists_empty(self):
        solution = Solution()
        list1 = None
        list2 = None
        expected = None
        self.assertEqual(solution.mergeTwoLists(list1, list2), expected)

    def test_one_list_empty(self):
        solution = Solution()
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = None
        expected = list1
        self.assertEqual(solution.mergeTwoLists(list1, list2).__dict__, expected.__dict__)

    def test_different_lengths(self):
        solution = Solution()
        list1 = ListNode(1, ListNode(3, ListNode(5)))
        list2 = ListNode(2, ListNode(4, ListNode(6, ListNode(7))))
        expected_vals = [1, 2, 3, 4, 5, 6, 7]
        merged_list = solution.mergeTwoLists(list1, list2)
        result = []
        while merged_list:
            result.append(merged_list.val)
            merged_list = merged_list.next
        self.assertEqual(result, expected_vals)

    def test_different_orders(self):
        solution = Solution()
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        expected_vals = [1, 1, 2, 3, 4, 4]
        merged_list = solution.mergeTwoLists(list1, list2)
        result = []
        while merged_list:
            result.append(merged_list.val)
            merged_list = merged_list.next
        self.assertEqual(result, expected_vals)

if __name__ == '__main__':
    unittest.main()