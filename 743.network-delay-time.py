#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        q = [K,0]
        max_dist = 0
        dict ={}
        for item in times:
            if item[0] not in dict:
                dict[item[0]]=[item]
            else:
                dict[item[0]].append(item)
        while len(q)>0:
            node,d = q.pop(0)
            for item in dict[node]:
                x,y,dist = item
                q.append([y,dict])
                


