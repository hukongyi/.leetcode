#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30112
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1]*n
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]

# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#
