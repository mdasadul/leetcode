#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
       
        l=0
        h = len(letters)-1 
        while(l<=h):
            mid = (l+h)>>1#l+(h-l)//2 
            if target>=letters[mid]:
                l = mid + 1 
            else:
                h = mid -1 
        if l<len(letters):
            return letters[l]
        else:
            return letters[0]

