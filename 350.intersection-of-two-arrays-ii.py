#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d2 = {}
        for n in nums2:
            if n in d2:
                d2[n] +=1
            else:
                d2[n] = 1
        ret = []
        for item in nums1:
            if item in d2:
                ret.append(item)
                if d2[item]>1:
                    d2[item] -=1
                else:
                    del d2[item]
        return ret
