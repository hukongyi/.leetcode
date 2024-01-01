#
# @lc app=leetcode.cn id=435 lang=python3
# @lcpr version=30112
#
# [435] 无重叠区间
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return n - count


# @lc code=end


#
# @lcpr case=start
# [[1,2],[2,3],[3,4],[1,3]]\n
# @lcpr case=end

# @lcpr case=start
# [ [1,2], [1,2], [1,2] ]\n
# @lcpr case=end

# @lcpr case=start
# [ [1,2], [2,3] ]\n
# @lcpr case=end

#
