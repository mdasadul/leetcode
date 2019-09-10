# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return
        a = []
        node = head
        while(node):
            a.append(node.val)
            node = node.next
        l = len(a)
        k = k if k<l else k%l
        
        a=a[-k:]+a[:-k]
        head = None
        for item in a[::-1]:
            node = ListNode(item)
            if head:
                node.next = head
                head = node
            else:
                head = node
        return head
        
            
            