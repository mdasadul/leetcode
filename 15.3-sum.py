import bisect
class Solution:
    def threeSum(self, nums):
        nums.sort()
        array = []

        for  i in range(len(nums)-2):
            l = i+1 
            r = len(nums)-1
            while r>l:
                t = nums[i]+nums[l]+ nums[r]
                if t == 0:
                   n = [nums[i],nums[l],nums[r]]
                 
                   l +=1
                   r -=1
                   array.append(n)
                
                elif t>0:
                    r -=1
                else:
                    l +=1
        return set(tuple(a) for a in array)          
            
           