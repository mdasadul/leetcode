class BinarySearch(object):
    def __init__(self, arr):
        self.arr = arr
    def find_element(self,item):
        h = len(self.arr)
        l = 0
        m = h//2
        
        while(l<m):
            
            if item== self.arr[m]:
                return m
            elif item <self.arr[m]:
                h = m-1
                
            else:
                l = m+1 
            m = (l+h)//2 
            print(l,m,h)
        if len(self.arr)>m:
            if  self.arr[m]==item:
                return m
            elif self.arr[m]< item:
                return m+1,'ins' 
            else:
                return m-1,'ins'
        else:
            return m, 'ins'

obj =BinarySearch([1,2,4,6,9,11])
print(obj.find_element(0))