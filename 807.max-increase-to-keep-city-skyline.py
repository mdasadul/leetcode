#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#
# @lc code=start
import numpy as np
class Solution:
    
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ret = 0
        row_max =[max(row) for row in grid]
        col_max =[] 
        for i in range(len(grid)):
            col =[]
            for row in grid:
                col.append(row[i])
            col_max.append(max(col))

        rl = len(row_max)
        cl = len(col_max)
        for i in range(rl):
            for j in range(cl):
                ret +=min(row_max[i], col_max[j]) - grid[i][j]
        return ret                
# @lc code=end

