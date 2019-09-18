#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = collections.Counter(nums).most_common(1)
        h =[(v,k) for k,v in d]
        heapq.heapify(h)
        return heapq.heappop(h)[1]

