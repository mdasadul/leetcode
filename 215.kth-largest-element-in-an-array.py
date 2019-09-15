#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        nums = [-1*i for i in nums]
        heapq.heapify(nums)
        

        
