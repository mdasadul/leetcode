#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s=='': return 0
        items = set()
        for chr in s: 
            if chr not in items:
                items.add(chr)
            else:
                items.remove(chr) 
        sum = len(items)
        
            
        return len(s)-sum+1 if sum>0 else len(s)
    

