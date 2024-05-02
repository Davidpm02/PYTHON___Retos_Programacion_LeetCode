import unittest
from typing import *
from ..scripts.code import *

class TestMergeKLists(unittest.TestCase):
    def test_empty_lists(self):
        solution = Solution()
        self.assertEqual(solution.mergeKLists([]), None)

    def test_one_empty_list(self):
        solution = Solution()
        self.assertEqual(solution.mergeKLists([[]]), None)

    def test_two_empty_lists(self):
        solution = Solution()
        self.assertEqual(solution.mergeKLists([[], []]), None)

    def test_one_list(self):
        solution = Solution()
        lists = [[1, 2, 3]]
        self.assertEqual(solution.mergeKLists(lists), ListNode(1).append(ListNode(2).append(ListNode(3))))

    def test_two_lists(self):
        solution = Solution()
        lists = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(solution.mergeKLists(lists), ListNode(1).append(ListNode(2).append(ListNode(3))).append(ListNode(4).append(ListNode(5).append(ListNode(6)))))

    def test_three_lists(self):
        solution = Solution()
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        self.assertEqual(solution.mergeKLists(lists), ListNode(1).append(ListNode(1).append(ListNode(2))).append(ListNode(3).append(ListNode(4).append(ListNode(4).append(ListNode(5).append(ListNode(6)))))))

if __name__ == '__main__':
    unittest.main()