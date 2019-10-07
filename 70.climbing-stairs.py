#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
class Solution:
    def climbStairs(self, n: int) -> int:
        return round((((math.sqrt(5) + 1)/2)** n) / math.sqrt(5))
      
