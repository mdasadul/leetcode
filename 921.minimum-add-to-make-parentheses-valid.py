#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack)
# @lc code=end

