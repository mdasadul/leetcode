"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root==None: return
        r_val=[]
        queue=[root]
        while(queue !=[]):
            c_val = []
            next_queue=[]
            for item in queue:
                c_val.append(item.val)
                for child in item.children:
                    next_queue.append(child)
            queue = next_queue
            r_val.append(c_val)
        return r_val
        