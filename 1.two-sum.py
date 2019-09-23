#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = nums.copy()
        l = 0
        nums.sort()
        r = len(nums)-1
        # print(n)
        ret = []
        while l < r:
            sum_ = nums[l] + nums[r]
            # print(sum_)
            if target ==sum_:
               return [n.index(nums[l]),len(n)-1-n[::-1].index(nums[r])]
            elif target > sum_:
               l += 1
            else:
                r -= 1
            
            

