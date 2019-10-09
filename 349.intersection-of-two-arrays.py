#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1)&set(nums2)

