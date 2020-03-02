#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        hash ={}
        m = n
        while True:
            s = 0
            for i in str(m):
                s+=int(i)**2
            m = s
            if m not in hash:
                hash[m]=m
            else:
                return False
            if m ==1:
                return True
            
        
# @lc code=end

