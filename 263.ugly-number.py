#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
class Solution:
    def isUgly(self, num: int) -> bool:
        if num==0: return False
        if num ==1: return True

        while True:
            if num ==1: return True
            elif num %30 ==0:
                num = num//30
            elif num%15 ==0:
                num = num//15
            elif num%5==0: 
                num = num//5 
            elif num%3 ==0: 
                num = num//3
            elif num%2 ==0:
                num = num//2 
            else:
                return False
        return True
