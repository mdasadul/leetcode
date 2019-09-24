import bisect
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        array = []
        min_val = float('inf')
        h = float('inf')
        print(nums)

        for  i in range(len(nums)-2):
            l = i+1 
            r = len(nums)-1
            while r>l:
                t = nums[i]+nums[l]+ nums[r]
                # print(nums[i],nums[l],nums[r])
                # print(t, min_val)
                if abs(target-t) < min_val:                   
                    
                    min_val = abs(target-t)
                    h = t
                
                
                if abs(target - (nums[i]+nums[l+1]+ nums[r]))< abs(target - (nums[i]+nums[l]+ nums[r-1])):
                    l = l+1
                else:
                    r = r-1
                    
        return h