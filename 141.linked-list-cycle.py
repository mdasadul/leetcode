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
        d ={}
        while head: 
            if head not in d:
                d[head] = 1 
            else:
                return True
            head = head.next
        return False
    
    



