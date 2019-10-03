#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = {}
        for index, item in enumerate(nums):
            if item in hashtable:
                hashtable[item].append(index)
            else:
                hashtable[item] = [index]
        for key,value in hashtable.items():
            if len(value)>1:
                for i in range(len(value)-1):
                    if (value[i+1]-value[i])<=k:
                        return True
        return False
# @lc code=end

