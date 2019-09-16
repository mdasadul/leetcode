#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums =collections.Counter(nums)
        h = []
        h=[(-v,k) for k,v in nums.items()]
        heapq.heapify(h)
        ret = []
        for _ in range(k):
            v,k = heapq.heappop(h)
            ret.append(k)
        return ret
