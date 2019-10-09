#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        for index, item in enumerate(nums2):
            h[item] = index
        ret = []
        l = len(nums2)
        for item in nums1:
            index = h[item]
            ii = index+1
            while   l>ii:
                if nums2[ii]>item:
                        ret.append(nums2[ii])
                        break
                ii +=1
            else:
                ret.append(-1)
        return ret
