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
        head = None
        forward = None
        if l1==None and l2==None:
            return 
        while l1 and l2:
            node = ListNode(None)
            if l1.val > l2.val:
                node.val = l2.val
                l2 = l2.next
            else:
                node.val =l1.val
                l1 = l1.next
            if head==None:
                head = node
                forward = node
            else:
                forward.next = node
                forward = node
        h = l1 or l2
        if forward:
            forward.next =h
        else:
            head = h
        return head
                
            
        
        

