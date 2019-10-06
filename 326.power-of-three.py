#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n ==0: return False
        if n==1: return True

        while n:
            if n ==3 : return True
            if n%3 ==0: 
                n = n//3 
            else:
                return False
        return True

