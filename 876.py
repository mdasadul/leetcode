# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=[]
        node = head
        while(node):
            a.append(node.val)
            node = node.next
        l = len(a)//2
        i =0
        while(head):
            if i ==l:
                return head
            i+=1
            head = head.next
        
        
            
        
        