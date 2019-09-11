class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return 
        l = len(nums)
        k = k%l
        if k>0:
            nums[:] =nums[-k:]+nums[:-k]

    

