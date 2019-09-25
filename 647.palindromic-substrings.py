#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        if s=="":
            return 0
        l = len(s)
        if l<2:
            return 1
        dp = [[0]*l for _ in range(l)]
        ret = 0
        for k in range(l):
            for i,j in zip(range(l-k),range(k, l)):
                if i == j: 
                    dp[i][j] = 1
                elif i+1 ==j and s[i]==s[j]:
                    dp[i][j]= 1
                elif j - i>1 and s[i]==s[j]:
                    dp[i][j]= dp[i+1][j-1]
                if dp[i][j] == 1: ret += 1
        return ret
                
                    
            
