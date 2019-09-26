#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=''
        for i in range(len(S)):
            if stack and stack[-1]==S[i]:
                stack = stack[:-1]
            else:
                stack +=S[i]
        return stack
            
            