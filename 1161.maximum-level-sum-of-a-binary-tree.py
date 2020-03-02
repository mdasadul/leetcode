#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        d = []
        label_nodes = [root]
        while label_nodes:
            temp_list = []
            label_val = 0
            for node in label_nodes:
                label_val+=node.val
                if node.left:
                    temp_list.append(node.left)
                if node.right:
                    temp_list.append(node.right)
            label_nodes = temp_list
            d.append(label_val)
        return d.index(max(d))+1
            
            
# @lc code=end

