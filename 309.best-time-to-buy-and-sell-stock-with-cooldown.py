#
# @lc app=leetcode.cn id=309 lang=python3
# @lcpr version=30112
#
# [309] 买卖股票的最佳时机含冷冻期
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in prices]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = dp[i - 1][1]
        return max(dp[-1][1:])


# @lc code=end


#
# @lcpr case=start
# [1,2,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
