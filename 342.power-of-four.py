#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n ==0: return False
        if n==1: return True

        while n:
            if n ==4 : return True
            if n%4 ==0: 
                n = n//4 
            else:
                return False
        return True
       

