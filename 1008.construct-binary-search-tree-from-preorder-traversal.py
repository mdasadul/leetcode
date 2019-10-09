#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for item in preorder:
            node = TreeNode(item)
            if not root:
                root = node
            else:
                par =ptr = root
                while ptr:
                    par = ptr
                    if item>ptr.val:
                        ptr = ptr.right
                    else:
                        ptr = ptr.left
                if item> par.val:
                    par.right = node
                else:
                    par.left = node
        return root
                
# @lc code=end

