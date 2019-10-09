#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      return list(collections.Counter(t)-collections.Counter(s))[0]
            
