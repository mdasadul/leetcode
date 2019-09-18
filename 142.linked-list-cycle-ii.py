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
        if not head: return None
        
        while head: 
            head.val = [head.val,None]
            head = head.next
            if head and type(head.val) is list:
                break
        if head: 
            head.val = head.val[0]
            return head
        else:
            None
    


