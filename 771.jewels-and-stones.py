#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d={}
        for item in S:
            if item not in d:
                d[item] =1
            else:
                
                d[item] += 1
        ret = 0
        for item in J:
             ret +=d.get(item,0)
        return ret
