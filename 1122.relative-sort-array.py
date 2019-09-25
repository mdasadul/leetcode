#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for item in arr1:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1
        ret =[]
        for item in arr2:
            ret+=[item]*d[item]
            d[item]=0
        print(d)
        q = []
        for key,value in d.items():
            q+=[key]*value
        q.sort()
        ret = ret + q
        return ret

