#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even =[]
        odd = []
        for item in A:
            if item%2  ==0:
                even.append(item)
            else:
                odd.append(item)
        ret = []
        for e,o in zip(even,odd):
            ret.append(e)
            ret.append(o)
        return ret



