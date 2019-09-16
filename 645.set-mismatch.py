#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d =  collections.Counter(nums)
        h = []
        h=[(-v,k) for k,v in d.items()]
        heapq.heapify(h)
        ret = []
        
        v,k = heapq.heappop(h)
        i = 1
        for key,_ in zip(d.items():
            if i!=key:
                return [k,i]
            i +=1
            
