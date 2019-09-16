#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
class Solution:
    def frequencySort(self, s: str) -> str:
        s = collections.Counter(list(s))
        h =[]
        for k,v in s.items():
            heapq.heappush(h,(-v,k))
        ret =[]
        while h:
            v, k = heapq.heappop(h)
            ret +=[k]*(-v) 
        return ''.join(ret)
        
      

