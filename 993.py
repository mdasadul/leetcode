# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root,x,y):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None: return
        queue = [root]
        while(queue):
            temp_queue = []
            temp_level = []
            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                    temp_level.append(node.left.val)
                if node.right:
                    temp_queue.append(node.right)
                    temp_level.append(node.right.val)
                if  node.left and  node.right:
                    p= [node.left.val, node.right.val]
                    if x in  p and y in p:
                        return False
                
                
            if temp_level:
                if x in temp_level and y in temp_level:
                    return True
            queue= temp_queue
                    