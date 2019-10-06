#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if str(bin(n)).count('1')>1 or n<=0: return False
        return True

