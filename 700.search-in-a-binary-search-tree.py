#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and root.val < val: return self.searchBST(root.right, val)
        elif root and root.val > val: return self.searchBST(root.left, val)
        else: return root        
                    
# @lc code=end

