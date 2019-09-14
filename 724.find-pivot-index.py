#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if nums==[]: return -1
        # if len(nums=>2):
        #     if sum(nums[1:]==0)
        for num, i in enumerate(nums[1:-1]):
           if ( sum(nums[:i])==sum(nums[i+1:])):
               return i 
            
        return -1

