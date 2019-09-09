
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None: return
        queue =[root]
        post_order =[[root.val]]
        level = 1
        while(len(queue)>0):
            temp_list = []
            new_queue=[]
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                    temp_list.append(node.left.val)
                if node.right:
                    new_queue.append(node.right)
                    temp_list.append(node.right.val)
            if temp_list!=[]:
                level +=1
                if level%2==0:
                    temp_list = temp_list[::-1]
                post_order.append(temp_list)
            queue = new_queue
                
        return post_order

