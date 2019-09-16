#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i,j in collections.Counter(nums).most_common(k)]
        # h = []
        # h=[(-v,k) for k,v in nums.items()]
        # heapq.heapify(h)
        # ret = []
        # for _ in range(k):
        #     v,k = heapq.heappop(h)
        #     ret.append(k)
        # return ret
