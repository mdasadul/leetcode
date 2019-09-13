#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder and postorder:
            item = postorder.pop()
            node = TreeNode(item)
            i = inorder.index(item)
            node.right =self.buildTree(inorder[i+1:], postorder)
            node.left =self.buildTree(inorder[:i], postorder)
            return node

