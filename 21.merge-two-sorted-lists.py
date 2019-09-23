#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val:
                node.val = l2.val
                list1.append(l2.val)
                l2 = l2.next
            else:
                list1.append(l1.val)
                l1 = l1.next
            
        
        

