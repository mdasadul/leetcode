#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d =  collections.Counter(nums)
        l = len(nums)
        h = []
        h=[(-v,k) for k,v in d.items()]
        heapq.heapify(h)
        ret = []
        
        v,k = heapq.heappop(h)

        for i in range(1,l+1):
            if i not in d:
                return [k,i]
    
            
