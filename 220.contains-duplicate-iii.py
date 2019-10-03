#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0 or k<0:
            return False
        
        if t==0 and len(nums)==len(set(nums)):
            return False
        hashtable = collections.OrderedDict()
        for index, item in enumerate(nums):
            if item in hashtable:
                hashtable[item].append(index)
            else:
                hashtable[item] = [index]
        #hashtable = collections.OrderedDict(sorted(hashtable.items(), key=lambda x: x[0]))
        
        key_list =[]
        
        for key,value in hashtable.items():
            if len(value)>1:
                for i in range(len(value)-1):
                    if (value[i+1]-value[i])<=k and t>=0:
                        return True
            else:
                
                for i in range(len(key_list)):
                    if abs(key_list[i] - key)<=t and abs(hashtable[key][0]-hashtable[key_list[i]][0])<=k:
                        return True
            key_list.append(key)
            
        return False   
# @lc code=end

