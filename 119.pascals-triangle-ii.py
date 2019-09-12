#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex ==[]: return []
        prev_row=[1]
        for i in range(1,rowIndex+1):
            temp_list = [1]
            for j in range(1,i):
                temp_list.append(prev_row[j-1]+prev_row[j])
            temp_list.append(1)
            prev_row = temp_list
        return prev_row
