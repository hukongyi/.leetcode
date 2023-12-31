#
# @lc app=leetcode.cn id=1154 lang=python3
# @lcpr version=30112
#
# [1154] 一年中的第几天
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split("-")
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        daysofmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def ifrun(year):
            return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
        if month < 3:
            return sum(daysofmonth[:month-1])+day
        else:
            return sum(daysofmonth[:month-1])+day+int(ifrun(year))

# @lc code=end


#
# @lcpr case=start
# "2019-01-09"\n
# @lcpr case=end

# @lcpr case=start
# "2019-02-10"\n
# @lcpr case=end

#
