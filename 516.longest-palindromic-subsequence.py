#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        
        l = len(s)
        dp = [[0]*l for _ in range(l)]
        length =0
        
        for k in range(l):
            for i, j in zip(range(l-k),range(k, l)):
                if (i == j ):
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j]= max(dp[i+1][j],dp[i][j-1]) 
                if dp[i][j] >length:
                    length = dp[i][j]
        return length

