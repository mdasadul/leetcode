#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x^y 
        count = 0
        while x: 
            count += 1
            x = x & (x - 1)
        return count
        
# @lc code=end

