#
# @lc app=leetcode.cn id=115 lang=python3
# @lcpr version=30112
#
# [115] 不同的子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + dp[j][i - 1]
                else:
                    dp[j][i] = dp[j][i - 1]
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# "rabbbit"\n"rabbit"\n
# @lcpr case=end

# @lcpr case=start
# "babgbag"\n"bag"\n
# @lcpr case=end

#
