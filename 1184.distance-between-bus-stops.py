#
# @lc app=leetcode id=1184 lang=python3
#
# [1184] Distance Between Bus Stops
#
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start<destination:
            left = sum(distance[start:destination])
            
        else:
            left = sum(distance[destination:start])
        all = sum(distance)
        return min(left,all-left)
