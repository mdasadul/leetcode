class Solution:
    def del_max(self,nums):
        first_max = max(nums)
        for i in range(nums.count(first_max)):
            nums.remove(first_max)
        return nums
    def thirdMax(self, nums) :
        first_max = max(nums)
        hash = set()
        for item in nums: 
            if item not in hash:
                hash.add(item)
        if len(hash)<=2: return first_max
        for i in range(2):
            nums = self.del_max(nums)
        return max(nums)
                    
      