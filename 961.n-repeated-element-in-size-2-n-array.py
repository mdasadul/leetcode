#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        l = len(A)
        d = {}
        for i in A:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
            if d[i]==l/2:
                return i
        
# @lc code=end

