#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        num_dict =collections.Counter(nums)
        freq = 0
        for item in sorted(num_dict.keys(), reverse = True):
            freq += num_dict[item]
            if k-freq<=0:
                return item
        
        
        
