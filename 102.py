
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root==None: return
        queue =[root]
        post_order =[[root.val]]
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
                post_order.append(temp_list)
            queue = new_queue
                
        return post_order

