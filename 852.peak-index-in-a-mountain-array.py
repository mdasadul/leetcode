#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for index, item in enumerate(A[1:],1):
            if A[index-1]>item:
                return index-1
        
            
