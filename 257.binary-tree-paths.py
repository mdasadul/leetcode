#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        queue = [root]
        path = []
        
        dict_arr ={}
        i=1
        while(len(queue) > 0):
            node = queue.pop()
            dict_arr[i]=node
            if  node.left and node.right:
                queue.append(node.right)
                queue.append(node.left)
                dict_arr[2*i] = node.left
                dict_arr[2*i+1] = node.right
            elif node.left :
                queue.append(node.left)
                dict_arr[2*i] = node.left
                dict_arr[2*i+1] = None
            elif node.right:
                queue.append(node.right)
                dict_arr[2*i+1] = node.right
                dict_arr[2*i] = None
            else:
                dict_arr[2*i+1] = None
                dict_arr[2*i] = None
            i +=1 
        print(dict_arr)  
        j=i
        for i in range(1,i+1):
            if dict_arr[i]!=None and  dict_arr[2*i]==None and dict_arr[2*i+1]==None: 
                paths.append('->'.join([str(dict_arr[i].val) if dict_arr[i].val is not None for j range(i+1)]))
                dict_arr[i]=None
            i = i+1
        print(paths)
            
                
# @lc code=end

