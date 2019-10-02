#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for item in arr:
            if item not in h:
                h[item] =1 
            else:
                h[item] += 1
        val =h.values()
        return len(val) == len(set(val))
# @lc code=end

