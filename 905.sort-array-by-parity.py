#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even =[]
        odd = []
        for item in A:
            if item%2  ==0:
                even.append(item)
            else:
                odd.append(item)
        
        return even+odd
