#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        numRows= len(grid)
        numCols  = len(grid[0])
        if grid[0][0]==1: return -1
        q = [(0,0,1)]
        while len(q)>0:
            x,y,d = q.pop(0)
            if x==numRows-1 and y==numCols-1:
                return d
            for a,b in ((x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x,y+1),(x,y-1),(x+1,y),(x-1,y)):
                if 0<=a<numRows and 0<=b<numCols and grid[a][b]==0:
                    grid[a][b]=1 
                    q.append((a,b,d+1))
        return -1 
