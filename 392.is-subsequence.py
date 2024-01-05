#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30112
#
# [392] 判断子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]==len(s)


# @lc code=end


#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#
