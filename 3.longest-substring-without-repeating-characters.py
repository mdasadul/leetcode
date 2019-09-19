#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='': return 0
        max_length =1
        
        for i in range(len(s)):
            sub =''
            for item in s[i:]:
                if item in sub:
                    sub +=item
                else:
                    if max_length<len(sub):
                        max_length = len(sub) 
                    sub = item
            if max_length<len(sub):max_length=len(sub)
        return max_length

