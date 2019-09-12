#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder and inorder:
            item = preorder.pop(0)
            tree = TreeNode(item)
            i = inorder.index(item)
            tree.left = self.buildTree(preorder,inorder[:i])
            
            tree.right = self.buildTree(preorder,inorder[i+1:])
            return tree
