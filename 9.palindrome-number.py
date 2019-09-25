#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        l = len(num)
        p=num[:l//2]
        m = num[l//2:][::-1]
        for i in range(len(num)//2):
            if m[i] !=p[i]:
                return False
        return True
