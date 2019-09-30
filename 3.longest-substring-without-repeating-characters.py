#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='': return 0
        max_length =1
        d = set()
        max_length = 0
        length = 0
        sub_str=''
        for i in s:
            if i not in d: 
                length += 1 
                d.add(i)
                sub_str +=i
            else: 
                    sub_str = sub_str[sub_str.index(i)+1:]+i
                    length =len(sub_str)
                    d=set(sub_str)
            if max_length < length:
                    max_length = length 
            
        return max_length
