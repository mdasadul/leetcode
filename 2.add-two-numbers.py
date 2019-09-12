#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        l3 = None
        head = None
        remainder = 0
        prev_remainder =0
        while(l1 or l2):
            sum_ = (l1.val if l1 else 0) + (l2.val if l2 else 0) + prev_remainder
            if sum_>=10:
                remainder =sum_//10
                sum_ =sum_%10

            node = ListNode(sum_)
            if l3:
                l3.next = node
                l3 = node
            else:
                head = l3 = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            prev_remainder = remainder
            remainder = 0
        if prev_remainder>0:
            l3.next = ListNode(prev_remainder)

        return head

