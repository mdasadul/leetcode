#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
import pdb 
import bisect
class Solution:
    def threeSum(self, nums):
        nums.sort(reverse=True)
        array = []
        for  i, item in enumerate(nums[:-2]):
            sum = item
            
            for index in range(i+1,len(nums)-1):
                x = -(sum + nums[index]) 
                p= bisect.bisect_left( nums[index+1:], x)
                if nums[p]==x:
                    array.append([-(item+nums[index]),nums[index],item])
                    a = [-(item+nums[index]),nums[index],item]
                    if a not in array:
                        array.append(a)
                    #break
                elif (x > nums[index+1]):
                    break

        return array
obj= Solution()
obj.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])