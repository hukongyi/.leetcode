#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30112
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] *len(prices) for _ in range(2)]
        dp[0][0] = -prices[0]
        dp[1][0]=0
        for i in range(1,len(prices)):
            dp[0][i] = max(dp[0][i-1],-prices[i])
            dp[1][i] = max(dp[1][i-1],dp[0][i-1]+prices[i])
        return dp[-1][-1]

# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

