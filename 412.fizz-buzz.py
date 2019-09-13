#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1,n+1):
            if i%15==0:
                ret.append("FizzBuzz")
            elif i%5==0:
                ret.append('Buzz')
            elif i%3==0:
                ret.append('Fizz')
            else:
                ret.append(str(i))
        
        # for i in range(3,n+1,3):
        #     ret[i-1]='Fizz'
        # for i in range(5, n+1, 5):
        #     ret[i-1] = 'Buzz'
        # for i in range(15, n+1,15):
        #     ret[i-1]='FizzBuzz'
        return ret 
