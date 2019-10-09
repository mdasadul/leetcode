#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        h = {}
        for index, item in enumerate(arr):
            if item-difference in h:
                h[item] = 1+h[item - difference]
            else:
                h[item] = 1
       
        return max(h.values())
        

