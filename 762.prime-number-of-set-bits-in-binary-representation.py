#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        counter = 0
        prime = [2,3,5,7,11,13,17,19]
        for i in range(L,R+1,1):
            if str(bin(i)).count('1') in prime:
                counter+=1
        return counter   

