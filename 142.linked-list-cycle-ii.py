#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = {}
        counter = 0
        while head: 
            if head in d:
                return head
            d[head] = counter

            counter += 1
            head = head.next
        return None


