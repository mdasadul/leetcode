#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        nums =  collections.Counter(words)
        h = []
        h=[(-v,k) for k,v in nums.items()]
        heapq.heapify(h)
        ret = []
        for _ in range(k):
            v,k = heapq.heappop(h)
            ret.append(k)
        return ret       

