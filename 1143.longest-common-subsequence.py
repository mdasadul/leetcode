#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s = text1+text2[::-1]
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        length  = 0
        for k in range(n):
            for i,j in zip(range(n-k),range(k, n)):
                if i == j:
                    dp[i][j] = 1
                elif s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                if dp[i][j]>length:
                   length = dp[i][j]
        return length//2 
