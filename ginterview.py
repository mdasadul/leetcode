class Solution(object):
    def planting(self, nums, k):

            l = len(nums)
            steps = 0
            n=k
            while l>1:
                steps += l
                k = n
                trees = 0
                i = 1
                while( l>1 and (k-nums[l-i])>=nums[l-i-1]):
                    trees +=1
                    k = k-nums[l-i]
                    i = i+1 
                    
                steps +=l-trees
                l = l-1
                l = l - trees

            return steps
obj = Solution()
obj.planting([2, 4, 5, 1, 2],6)
