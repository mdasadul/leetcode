#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(str(bin(num)))-2)-1-num
        
        
