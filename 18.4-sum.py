#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        array = []
        # print(nums)
        for j in range(len(nums)-3):

            for  i in range(j+1,len(nums)-2):
                l = i+1
                
                r = len(nums)-1
                while r>l:
                    q = [nums[j],nums[i],nums[l], nums[r]]
                    t = sum(q)
                    if t == target:
                    
                        l +=1
                        r -=1
                        array.append(q)
                        
                    elif t>target:
                        r -=1
                    else:
                        l +=1
        return set(tuple(a) for a in array)          
            

