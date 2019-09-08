# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None: return 0
        queue = [root]
        depth = 1
        while(queue):
            temp_queue = []
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left :
                    temp_queue.append(node.left)
                if node.right:
                    temp_queue.append(node.right)
                
            queue= temp_queue
            depth +=1
            