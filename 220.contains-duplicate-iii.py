#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 | k<0:
            return False
        
        if t==0 and len(nums) ==len(set(nums)):
            return False
        
        for i in range(len(nums)):
            
            j=i+1
            while (j<min(i+k+1,len(nums))):
                if abs(nums[i]-nums[j])<=t:
                    return True
                j +=1
        return False


