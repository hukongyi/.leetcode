#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30112
#
# [56] 合并区间
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = list()
        begin = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                ans.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        ans.append([begin, end])
        return ans


# @lc code=end


#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[2,3]]\n
# @lcpr case=end

#
