# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    global_max= - float('inf')
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.root_toany(root)
        return self.global_max
    def root_toany(self, root):
        if root==None: return 0
        
        left = self.root_toany(root.left)
        right = self.root_toany(root.right)
        
        root_val = root.val
        left_val = left+ root_val
        right_val = right+ root_val
        left_right_root_val = root_val+ left+right
        
        return_val = max(root_val, left_val, right_val)
        
        local_max = max(return_val, left_right_root_val)
        self.global_max = max(self.global_max, local_max)
        return return_val
        