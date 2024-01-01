#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30112
#
# [122] 买卖股票的最佳时机 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0
        # for i in range(1,len(prices)):
        #     ans += max(prices[i]-prices[i-1],0)
        # return ans
        # method 2
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]+prices[i])
        return dp[-1][1]
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

