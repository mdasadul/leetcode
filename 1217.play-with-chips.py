#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Play with Chips
#
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = 0
        odd = 0
        for item in chips:
            if item%2==0:
                even +=1
            else:
                odd +=1
        return min(even,odd)
