#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        h_s = {}
        for i in t:
            if i in h_s:
                h_s[i] +=1
            else:
                h_s[i] = 1
        for item in s:
            if item in h_s:
                h_s[item] -=1
                if h_s[item]==0:
                    del h_s[item]
        return (list(h_s.keys())[0])
            
