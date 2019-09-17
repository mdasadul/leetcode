#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left =0
        right = len(A)
        while left < right:
            mid = left +(right-left)//2
            if (A[mid]<A[mid+1]):
                left = mid+1
            else:
                right = mid
        return left

                
        
            
