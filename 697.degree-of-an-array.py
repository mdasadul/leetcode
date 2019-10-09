#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        sorted_list = collections.Counter(nums).most_common()
        k,v = sorted_list[0]
        if v ==1: return 1
        l = (len(nums)-nums[::-1].index(k)) - nums.index(k)
        for pair in sorted_list[1:]:
            
            if v==pair[1]:
                k,v = pair
                t = (len(nums)-nums[::-1].index(k)) - nums.index(k)
                if t<l:
                    l = t
            else:
                break
        return l
# @lc code=end

