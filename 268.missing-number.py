#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # d ={}
        # for item in nums:
        #     d[item] = d[item]+1 if item in d else 1
        # for item in range(len(nums)+1):
        #     if item not in d:
        #         return item
        l = len(nums)
        return l*(l+1)//2 - sum(nums)

