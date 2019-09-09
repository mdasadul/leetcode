# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        nums =[]
        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
        inorder(root)
        nums.append(val)
        
        def constructMaximumBinaryTree(nums):
            if nums==[]: return

            max_val = max(nums)
            n = TreeNode(max_val)
            n.left = constructMaximumBinaryTree(nums[:nums.index(max_val)])
            n.right = constructMaximumBinaryTree(nums[nums.index(max_val)+1:])
            return n
        return constructMaximumBinaryTree(nums)