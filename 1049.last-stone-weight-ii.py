#
# @lc app=leetcode.cn id=1049 lang=python3
# @lcpr version=30112
#
# [1049] 最后一块石头的重量 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        half_sum = stones_sum//2
        dp = [[0]*(half_sum+1) for _ in range(len(stones))]
        if stones[0] <= half_sum:
            dp[0][stones[0]] = 1
        for i in range(len(stones)):
            dp[i][0] = 1
        for i in range(1, len(stones)):
            for j in range(half_sum+1):
                if j < stones[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i]]
        for j in range(half_sum, -1, -1):
            if dp[-1][j] == 1:
                return stones_sum-j*2

                # @lc code=end

                #
                # @lcpr case=start
                # [2,7,4,1,8,1]\n
                # @lcpr case=end

                # @lcpr case=start
                # [1,2]\n
                # @lcpr case=end

                #
