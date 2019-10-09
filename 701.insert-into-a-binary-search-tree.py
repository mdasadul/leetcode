#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        parent  = root
        old_root = root
        while root:
            parent = root
            if val>root.val:
                root = root.right
            else:
                root = root.left
        if not parent.left and parent.val> val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return old_root
               
# @lc code=end

