#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0: return "0"
        a = ''
        neg = True if num<0 else False
        num =abs(num)
        while num:
            a=str(num%7)+a
            num = num//7 
        if neg:
            return '-'+a 
        else:
            return a

