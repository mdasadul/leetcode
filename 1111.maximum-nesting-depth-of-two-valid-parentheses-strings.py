#
# @lc app=leetcode id=1111 lang=python3
#
# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
#
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack =[]
        ret=[0]*len(seq)
        for index, item in enumerate(seq[:-1],1):
                if seq[index -1]==seq[index]:
                    ret[index] = 1-ret[index-1]
                else:
                    ret[index] = ret[index-1]
        return ret
