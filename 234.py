# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        data =[]
        while(head):
            data.append(head.val)
            head = head.next
        
        l = len(data)
        if l==1: return True
        rev_data=data[-(l//2):][::-1]
        data = data[:l/2]
        
            
        return data==rev_data
        