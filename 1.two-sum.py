#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, item in enumerate(nums):
            if target - item in hash:
                return [hash[target-item],index]
            hash[item] = index
       
            

