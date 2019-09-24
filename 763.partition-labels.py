#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        i = 0
        j = len(S)-1 
        ret = []
        right =''
        while i<len(S):
            k=i
            if S[i:][::-1].find(S[i]) >-1:
                j=len(S)-S[i:][::-1].index(S[i])
                
                part = set(S[i:j])
                i=j
                j = 0
                p=0
                vv=''
                for item in S[i:]:
                    #print(item)
                    if item not in part:
                        vv +=item 
                        p +=1
                        
                    else:
                        for ii in vv:
                            part.add(ii)
                        j+=p+1
                        p=0
                      
                i+=j 
                
                ret.append(i-k)
        return ret

