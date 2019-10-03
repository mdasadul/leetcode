#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> int:
        if not root: return False
        queue = [(root, [root.val])]
        counter = 0
        while queue:
            node, path = queue.pop()
            if node.left:
                queue.append((node.left, path+[node.left.val]))
            if node.right:
                queue.append((node.right, path+[node.right.val]))
            if not node.left and not node.right:
                temp_sum = sum_
                for item in path:
                    if sum_-item==0:
                        counter +=1
                        break 
                    elif sum_ - item> 0:
                        sum_ = sum_ - item
                    else:
                        sum_ = temp_sum
                    #10m 6, 5,3


                if sum_==sum(path):
                    return True
        return False


