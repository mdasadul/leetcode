class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rval=[]
        for i in range(left,right+1):
            number = i
            while(number):
                p = number%10
                if p==0:
                    break
                elif i % p != 0:
                    break
                number = number//10

            if not number:
                rval.append(i)
        return rval