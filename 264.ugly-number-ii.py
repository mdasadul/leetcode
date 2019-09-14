#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# 1,2,4,8,10,12,
# 1,3,6,9,12,15
# 1,5,10,15,20
# 1,2,3,5,6,8,9,10,12,
class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
        a=[1]
        i,j,k = 0,0,0
        while len(a)<n:
            val = min(a[i]*2,a[j]*3,a[k]*5)
            if val ==a[i]*2:
                i +=1
            elif val ==a[j]*3:
                j +=1
            elif val ==a[k]*5:
                k +=1
            if val > a[-1]:
                a.append(val)
            
        return a[-1]
