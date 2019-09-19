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
            m = (l+h)>>1 
            if target ==nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                h = m - 1
        return -1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(len(numbers)-1,0,-1):
            new_target = target - numbers[index]
            next_index = self.binary_search(numbers[:index], new_target)
            if next_index >= 0:
                return [ next_index+1,index + 1,]
            
