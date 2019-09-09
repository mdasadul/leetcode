class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        s = (re.sub(r'\W+','',s)).lower()
        r = s[::-1]
        
        return r==s
        