"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None: return
        queue =[root]
        post_order =[]
        while(len(queue)>0):
            node = queue.pop()
            post_order.append(node.val)
            queue +=node.children
        return post_order[::-1]

