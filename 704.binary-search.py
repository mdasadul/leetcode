#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        h = n-1
        while(l<=h):
            m = l + (h-l)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                h = m - 1
        return  -1

