#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30112
#
# [279] 完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n+1))
        i=2
        i2 = i*i
        while i2<=n:
            for j in range(i2,n+1):
                dp[j]=min(dp[j],dp[j-i2]+1)
            i+=1
            i2 = i*i
        return dp[-1] 
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end
#

