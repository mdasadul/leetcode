# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        orig_head,temp_head = None, head
        prev = None
        last=None
        i =1
        while head:
            if i<m:
                prev = head
            if i>=m and i<=n:
                node = ListNode(head.val)
                
                if orig_head:
                    node.next = orig_head
                    orig_head = node
                else:
                     orig_head = node
                     last=node                    
            elif i>n:
                
                
                return temp_head
            i +=1
            head = head.next
        if i>n:
                if prev:
                    prev.next = orig_head
                else:
                    temp_head = orig_head
             
            
        return temp_head
        
        
                
                
                