#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            return (digits[:-1]+[digits[-1]+1])
        else:
            new_digits =[]
            flag = True
            for item in digits[::-1]:
                if item==9 and flag: 
                    new_digits.append(0)
                elif flag:
                    new_digits.append(item+1)
                    flag = False
                else:
                    new_digits.append(item)
                    flag = False
            if flag:
                new_digits.append(1)
            return new_digits[::-1]

