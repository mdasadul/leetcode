#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
class Solution:
    def binary_search(self, nums, target):
        n = len(nums)
        l, h = 0, n-1 
        while(l <=h):
            if target ==nums[l]+nums[h]:
                return [l+1,h+1]
            elif target > nums[l]+nums[h]:
                l = l+1
            else:
                h = h - 1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            return self.binary_search(numbers, target)
