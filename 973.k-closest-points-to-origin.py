#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points =[[(item[0]**2+item[1]**2),item] for item in points]
        heapq.heapify(points)
        ret = []
        for _ in range(K):
            _, temp = heapq.heappop(points)
            ret.append(temp)
        return ret
    
