#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0
        ret = ""
        carry = 0
        while i < max(len(a),len(b)) or carry > 0 :
            aB = 0
            bB = 0
            if i < len(a):
                aB = int(a[len(a) - i - 1])
            if i < len(b):
                bB = int(b[len(b) - i - 1])
            ret = str(aB ^ bB ^ carry) + ret
            carry = ((aB ^ bB ) & carry) | (aB & bB)
            i += 1
        return ret  



