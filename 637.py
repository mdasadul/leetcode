
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None: return
        queue = [root]
        levels = [root.val]
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
                
            if temp_level:
                levels.append(1.0*sum(temp_level)/len(temp_level))
            queue= temp_queue
        return levels
                