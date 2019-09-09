# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums==[]: return
        
        max_val = max(nums)
        n = TreeNode(max_val)
        n.left = self.constructMaximumBinaryTree(nums[:nums.index(max_val)])
        n.right = self.constructMaximumBinaryTree(nums[nums.index(max_val)+1:])
        return n
            