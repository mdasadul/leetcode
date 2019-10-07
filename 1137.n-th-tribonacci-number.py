#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0: return 0
        h={0:0,1:1,2:1}
        for i in range(3,n+1):
            h[i] = h[i-1]+h[i-2]+h[i-3]
        return h[n]
