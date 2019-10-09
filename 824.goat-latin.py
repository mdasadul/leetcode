#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set('AEIOUaeiou')
        ret =[]
        for index, word in enumerate(S.split()):
            if word[0]in vowel:
                ret.append(word+'ma'+"a"*(index+1))
            else:
                ret.append(word[1:]+word[0]+'ma'+'a'*(index+1))
        return ' '.join(ret)

