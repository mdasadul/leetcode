#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
class Solution:
    def frequencySort(self, s: str) -> str:
        s = collections.Counter(list(s))
        t =[]
        for k ,v in sorted(s.items(), key=lambda item:item[1], reverse = True) :
            t +=[k]*v
        return ''.join(t)
        
      

