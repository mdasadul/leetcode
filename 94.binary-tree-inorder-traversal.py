#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root: 
            return self.inorderTraversal(root.left)+\
            [root.val]+ \
            self.inorderTraversal(root.right)
        else:
            return []
