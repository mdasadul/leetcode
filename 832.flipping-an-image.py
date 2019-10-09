#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        for row in A:
            row = row[::-1]
            row = [0 if i ==1 else 1 for i in row]
            ret.append(row)
        return ret
# @lc code=end

