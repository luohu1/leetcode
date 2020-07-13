#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # head.next.next == head
        head_list = []
        while head:
            head_list.append(head)
            head = head.next
            if head in head_list:
                return True
        return False


# @lc code=end
