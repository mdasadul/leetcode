#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ret =[]
        for item in A:
            ret.append(item**2)
        return sorted(ret)

