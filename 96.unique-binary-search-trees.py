#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30112
#
# [96] 不同的二叉搜索树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return n
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]

# @lc code=end


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
