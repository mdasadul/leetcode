#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows<=0: return []
        triangle = [[1]]
        for i in range(1,numRows):
            items=[1]*(i+1)
            for j in range(1,i):
                items[j]=triangle[i-1][j-1]+triangle[i-1][j]
            triangle.append(items)
        return triangle
