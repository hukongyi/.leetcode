#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30112
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j],dp[j-coins[i]]+1)
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]

# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

