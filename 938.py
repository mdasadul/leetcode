# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def inorder(root, value, left, right):
            
            if root:
                value = inorder(root.left, value, left, right)
                if root.val>right:
                    return value
                elif root.val>=left:
                    value +=root.val
                
                value = inorder(root.right, value, left, right)
            return value
            
        return inorder(root,0, L, R)