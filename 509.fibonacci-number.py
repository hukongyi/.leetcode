#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=30112
#
# [509] 斐波那契数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0, 1]
        for _ in range(1, n):
            dp[1], dp[0] = dp[0]+dp[1], dp[1]
        return dp[1]
# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#
