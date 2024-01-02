#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30112
#
# [62] 不同路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, n):
            for j in range(m):
                if j != 0:
                    dp[j][i] = dp[j-1][i]+dp[j][i-1]
                else:
                    dp[j][i] = 1
        return dp[-1][-1]

# @lc code=end

#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#
