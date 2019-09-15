#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#
# [-1,2,4,5,6,7]
# -1+4+6 = 9
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        for index, item in enumerate(nums):
            if index%2  ==0:
                ret +=item
        return ret
