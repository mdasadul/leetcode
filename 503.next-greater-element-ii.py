#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []
        h = {}
        for index, item in enumerate(nums):
            h[item] = index
        ret = []
        l = len(nums)
        for item in nums:
            index = h[item]
            next_index = index+1
            while   next_index != index:
                if next_index==l: 
                    next_index = -1

                elif nums[next_index]>item:
                        ret.append(nums[next_index])
                        break
                next_index +=1
            else:
                ret.append(-1)
        return ret

