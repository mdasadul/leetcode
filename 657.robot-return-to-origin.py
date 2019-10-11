#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        l = 0
        r = 0
        u = 0
        d = 0
        for m in moves:
            if m =='U':
                u+=1
            elif m =='D':
                d +=1
            elif m =='L':
                l +=1
            else:
                r+=1
            
        return True if l==r and u ==d else False
            
              
# @lc code=end

