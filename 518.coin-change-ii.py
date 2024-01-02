#
# @lc app=leetcode.cn id=518 lang=python3
# @lcpr version=30112
#
# [518] 零钱兑换 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins))]

        for j in range(amount//coins[0]+1):
            dp[0][j*coins[0]]=1

        for i in range(1,len(coins)):
            for j in range(amount+1):
                if j<coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-coins[i]]
        # for i in range(len(coins)):
        #     print(dp[i])
        return dp[-1][-1]
# @lc code=end



#
# @lcpr case=start
# 5\n[1, 2, 5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[10]\n
# @lcpr case=end

#

