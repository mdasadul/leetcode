#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ''
        dict={'(':1,')':2,'[':3,']':4,'{':5,'}':6}
        for c in s: 
            if stack and dict[stack[-1]]+1==dict[c]:
                stack = stack[:-1]
            else:
                stack +=c 
        return True if not stack else False

