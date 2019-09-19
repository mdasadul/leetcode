class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left =None
        self.right =None
    
class Heap(object):
    def __init__(self):
        self.h =[]

    def push(self,val):
        for index, item in enumerate(self.h):
            if val <=item:
                break
        if index >= len(self.h):
            self.h.append(val)
        else:
            self.h = self.h[:index]+[val]+self.h[index:]
        
