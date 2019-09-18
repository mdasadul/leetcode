#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        p=head
        q = p.next
        while p!=q: 
            p = p.next
            q = q.next.next if q and q.next else None
        return True if q and p==q else False



