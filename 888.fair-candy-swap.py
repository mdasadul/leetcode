#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = (sum(B)-sum(A))//2
        B = set(B)
        for item in set(A):
            if item+diff in B:
                return [item,item+diff]
                
                
        

