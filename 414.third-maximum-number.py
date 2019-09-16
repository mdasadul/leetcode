class Solution:

    def thirdMax(self, nums) :
        
        hash = set()
        for item in nums: 
            if item not in hash:
                hash.add(item)
        if len(hash)<=2: return max(hash)
        
        hash.remove(max(hash))
        hash.remove(max(hash))
        return max(hash)
                    
      