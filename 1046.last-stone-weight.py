#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*item for item in stones]
        heapq.heapify(stones)
        while(len(stones)>=2):
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a !=b:
                heapq.heappush(stones, a-b)
        else:
            return -heapq.heappop(stones)
        
        
