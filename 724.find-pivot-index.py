class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if nums==[]: return -1
        left = 0
        right = sum(nums[1:])
        lens = len(nums)
        for i in range(lens):
            
            if (left == right):
               return i 
            left += nums[i]
            if (i+1)<lens:
                right -= nums[i+1] 
            else:
                return -1
            
        return -1