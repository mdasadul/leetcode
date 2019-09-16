#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h =[]
        for l in matrix:
            h+=l
        heapq.heapify(h)
        item = 0
        for _ in range(k):
            item = heapq.heappop(h)
        return item
