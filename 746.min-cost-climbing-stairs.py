#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f=[0]*len(cost)
        f[-1] = cost[-1]
        f[-2] = cost[-2]
        for i in range(len(cost)-3,-1,-1):
            f[i] = cost[i]+min(f[i+1],f[i+2])
        return min(f[0],f[1])
                

