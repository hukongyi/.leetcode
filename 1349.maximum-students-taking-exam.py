#
# @lc app=leetcode.cn id=1349 lang=python3
# @lcpr version=30112
#
# [1349] 参加考试的最大学生数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        a = [sum((c == '.') << j for j, c in enumerate(s)) for s in seats]

        @cache
        def dfs(i, j):
            if i == 0:
                lb = j & -j
                return dfs(i, j & ~(lb*3))+1 if j else 0
            res = dfs(i-1, a[i-1])
            s = j
            while s:
                if (s & (s >> 1)) == 0:
                    t = a[i-1] & ~(s << 1 | s >> 1)
                    res = max(res, dfs(i-1, t)+s.bit_count())
                s = (s-1) & j
            return res
        return dfs(len(seats)-1, a[-1])
        # @lc code=end

        #
        # @lcpr case=start
        # [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]\n
        # @lcpr case=end

        # @lcpr case=start
        # [[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]\n
        # @lcpr case=end

        # @lcpr case=start
        # [["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]]\n
        # @lcpr case=end

        #
