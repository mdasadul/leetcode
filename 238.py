class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[1]
        b=[1]
        for item,rev_item in zip(nums[:-1],nums[::-1][:-1]):
            a.append(a[-1]*item)
            b.append(b[-1]*rev_item)
        return [a*b for a,b in zip(a,b[::-1])]