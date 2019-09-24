#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            h ={}
            for index, item in enumerate(numbers):
                if target-item in h:
                    return [h[target-item]+1, index+1]
                h[item] =index
