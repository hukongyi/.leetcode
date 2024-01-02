#
# @lc app=leetcode.cn id=746 lang=python3
# @lcpr version=30112
#
# [746] 使用最小花费爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[-1]
# @lc code=end


#
# @lcpr case=start
# [10,15,20]\n
# @lcpr case=end

# @lcpr case=start
# [1,100,1,1,1,100,1,1,100,1]\n
# @lcpr case=end

#
