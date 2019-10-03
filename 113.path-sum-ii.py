#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root: return []
        queue = [(root, [root.val])]
        paths =[]
        while queue:
            node, path = queue.pop()
            if node.left:
                queue.append((node.left, path+[node.left.val]))
            if node.right:
                queue.append((node.right, path+[node.right.val]))
            if not node.left and not node.right:
                if sum_==sum(path):
                    paths.append(path)
        return paths


