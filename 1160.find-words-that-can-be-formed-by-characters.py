#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        ret = 0
        for char in chars:
            if char not in d:
                d[char] =1
            else:
                d[char] += 1
        
        for word in words:
            counter = 0
            for char in word:
                if char not in d or d[char]<word.count(char):
                    counter = 0
                    break
                else:
                    counter += 1
            ret +=counter
        return ret
