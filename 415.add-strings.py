#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1 = len(num1)
        l2  = len(num2)

        if l1>l2:
            num2+='0'*(l1-l2)
        else:
            num1+='0'*(l2-l1)
        ret = ''
        rem= 0
        for a,b in zip(num1,num2):
            sum= (int(a)+int(b)+rem)
            rem = sum//10
            ret +=str(sum%10)
        if rem>0:
            ret +=str(rem)
        return ret[::-1]

