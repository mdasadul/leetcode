class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def ispalindrome(string):
            middle = len(string)//2
            rev_str=string[::-1]
            not_palindrome=[]
            for i in range(middle+1):
                if string[i]!=rev_str[i]:
                    ret_string = string
                    if i >0:
                        ret_string=string[i:-i]
                    return False, ret_string
            return True,[]
        pal_flag,s=ispalindrome(s)
        print(s)
        if pal_flag or len(s)<=2:
            return True
        else:
            pal_flag,_=ispalindrome(s[1:])
            if not pal_flag:
                pal_flag,_=ispalindrome(s[:-1])
                return pal_flag
            else:
                    return True
        return False