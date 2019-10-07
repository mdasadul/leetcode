#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
class Solution:
    def fib(self, N: int) -> int:
        # phi = (1+math.sqrt(5))/2
        # return round((phi**N-(1-phi)**N)/math.sqrt(5))
        if N==0: return 0
        a = 0
        b = 1 
        for i in range(1,N):
            c = b 
            b = a+b 
            a = c 
        return b 

