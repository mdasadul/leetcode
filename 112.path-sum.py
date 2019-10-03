#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
        if not root: return False
        queue = [(root, [root.val])]
        while queue:
            node, path = queue.pop()
            if node.left:
                queue.append((node.left, path+[node.left.val]))
            if node.right:
                queue.append((node.right, path+[node.right.val]))
            if not node.left and not node.right:
                if sum_==sum(path):
                    return True
        return False

