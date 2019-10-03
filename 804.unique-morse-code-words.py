#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        h ={}
        for key, value in zip(string.ascii_lowercase, codes):
            h[key] = value
        s = set()
        for item in words:
            s.add(''.join([h[c]for c in item]))
        return len(s)
        
# @lc code=end

