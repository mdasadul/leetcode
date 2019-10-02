#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root==None: return []
        queue = [(root,[str(root.val)])]
        paths = []
        while len(queue)>0:
            
            node, path = queue.pop()
            #print(path)
            if node.right:
                queue.append((node.right, path+[str(node.right.val)]))
         
            if node.left:
                queue.append((node.left,path+[str(node.left.val)]))
            if not node.left and not node.right:
                paths.append('->'.join(path))
        return paths        

