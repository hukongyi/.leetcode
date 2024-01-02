#
# @lc app=leetcode.cn id=343 lang=python3
# @lcpr version=30112
#
# [343] 整数拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max(j, dp[j])*max(i-j, dp[i-j]))
        return dp[-1]
# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#
