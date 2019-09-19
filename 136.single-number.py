#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # d= {}
        # m = -1
        # for item in nums:
        #     if item in d:
        #         d[item] +=1
        #     else:
        #         d[item] =1
        #         m = item
        # for k,v in d.items():
        #     if v==1: return k
        return collections.Counter(nums).most_common()[-1][0]

