#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n<2:
            return s
        start,end,length = 0,0,0
        dp = [[0]*n for _ in range(n)]
        for k in range(n):
            for i,j in zip(range(n-k),range(k,n)):
                if i == j: dp[i][j] = 1 
                elif i+1==j and s[i]==s[j]:
                    dp[i][j]=1 
                elif j-i>1 and s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                
                if dp[i][j]==1 and j-i+1>length:
                    start = i 
                    end = j+1 
                    length =j-i
            #print(dp)
        return s[start:end]
