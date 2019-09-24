#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        
        h = len(height)-1
        max = float('-inf')
        while(l<=h):
            m =min(height[l],height[h])
            if m*(h-l) > max:
                max = m*(h-l)
            if height[l]>height[h]:
                h = h-1 
            else:
                l = l+1
        return max    

