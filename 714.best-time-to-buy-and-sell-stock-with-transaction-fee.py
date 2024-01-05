#
# @lc app=leetcode.cn id=714 lang=python3
# @lcpr version=30112
#
# [714] 买卖股票的最佳时机含手续费
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for _ in prices]
        dp[0][0] = -prices[0] - fee
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i]-fee)
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]


# @lc code=end


#
# @lcpr case=start
# [1, 3, 2, 8, 4, 9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,7,5,10,3]\n3\n
# @lcpr case=end

#
