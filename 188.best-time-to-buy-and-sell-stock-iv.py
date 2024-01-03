#
# @lc app=leetcode.cn id=188 lang=python3
# @lcpr version=30112
#
# [188] 买卖股票的最佳时机 IV
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * 2 * k for _ in prices]
        for i in range(k):
            dp[0][2 * i] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(k):
                if j != 0:
                    dp[i][2 * j] = max(
                        dp[i - 1][2 * j], dp[i - 1][2 * j - 1] - prices[i]
                    )
                else:
                    dp[i][2 * j] = max(dp[i - 1][2 * j], -prices[i])

                dp[i][2 * j + 1] = max(
                    dp[i - 1][2 * j + 1], dp[i - 1][2 * j] + prices[i]
                )
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# 2\n[2,4,1]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[3,2,6,5,0,3]\n
# @lcpr case=end

#
