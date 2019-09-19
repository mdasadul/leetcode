#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs ==[]: return ""
        strs = sorted(strs, key=len)
        s= strs[0]
        l =len(s)
        for i in range(len(s)):
            flag = True
            for item in strs:
                
                if s[:l-i] !=item[:l-i]:
                    flag = False
                    break
            if flag:
                return s[:l-i]
        return ''
