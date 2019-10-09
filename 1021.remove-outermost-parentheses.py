#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        premitive = ''
        temp_prem =''
        for c in S:
            temp_prem +=c
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            if not stack: 
                premitive +=temp_prem[1:-1]
                temp_prem ='' 
        return premitive
# @lc code=end

