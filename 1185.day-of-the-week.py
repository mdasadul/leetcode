#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
# 1   2   3 4 5 6 7 8 9 10 11 12 
#  11  12  1 2 3 4 5 6 7 8  9  10
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C.
        k = day 
        m = (month-3)%12+1
        D = year%100
        C = year//100
        if m>10: D = D-1
        f = k + (13*m-1)//5 + D + D//4 + C//4 - 2*C
        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return day[f%7]
