#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> int:
        if not root: return 0
        queue = [(root,[root.val])]
        counter = 0
        paths = {}
        while queue:
            node, path = queue.pop()
            if node.left:
                queue.append((node.left,path+[node.left.val]))
            if node.right:
                queue.append((node.right, path+[node.right.val]))
            if not node.left and not node.right:
                for index, item in enumerate(path):
                    sum = sum_
                    
                    for j in range(index,len(path)):
                        if sum-path[j] ==0:
                            
                            if tuple(path[:j+1]) not in paths:
                                paths[tuple(path[:j+1])]=1
                                counter +=1
                            break
                        elif (sum - path[j])> sum:
                            sum = sum-path[j]
                            
                        else:
                            break
                            
                        
            
        return counter
            # @lc code=end

