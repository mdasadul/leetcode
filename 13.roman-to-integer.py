#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
        "I":1,
        "V": 5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
        number = 0
        flag = False
        for index, item in enumerate(s):
            if flag:
                flag = False
                continue
            if item == "I" and index+1 < len(s):
                if s[index+1]=='V':
                    number +=4 
                    flag = True
                elif s[index+1]=='X':
                    number +=9 
                    flag = True
                else:    
                    number +=dictionary[item]
            elif item == "X" and index+1 < len(s):
                if s[index+1]=='L':
                    number +=40 
                    flag = True
                elif s[index+1]=='C':
                    number +=90 
                    flag = True
                else:    
                    number +=dictionary[item]
            elif item == "C" and index+1 < len(s):
                if s[index+1]=='D':
                    number +=400 
                    flag = True
                elif s[index+1]=='M':
                    number +=900 
                    flag = True
                else:    
                    number +=dictionary[item]
            else:
                number +=dictionary[item]    
        return number        
        
# @lc code=end

