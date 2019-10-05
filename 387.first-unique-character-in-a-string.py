#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for item in s: 
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        for index, item in enumerate(s):
            if d[item]==1: return index
        return -1

