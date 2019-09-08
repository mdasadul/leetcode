# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def postorder(root, value):
            if root:
                value= postorder(root.right, value)
                value +=root.val
                root.val= value
                value = postorder(root.left, value)
            return value
        
        postorder(root,0)
        return root