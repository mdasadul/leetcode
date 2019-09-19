#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
       
        for item in letters:
            if item>target:
                return item
        if item ==letters[-1]:
            return letters[0]       

