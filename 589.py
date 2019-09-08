
class Solution(object):
    
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None: return
        queue = [root]
        r_val = []
        while(len(queue)>0):
            node=queue.pop()
            r_val.append(node.val)
            queue +=node.children[::-1]
        return r_val
        