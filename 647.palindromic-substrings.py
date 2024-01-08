#
# @lc app=leetcode.cn id=647 lang=python3
# @lcpr version=30112
#
# [647] 回文子串
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in s]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-2,-1,-1):
            for j in range(i + 1, len(s)):
                if j == i + 1:
                    dp[i][j] = int(s[i] == s[j])
                else:
                    dp[i][j] = int((s[i] == s[j]) and (dp[i+1][j - 1]))
        return sum(map(sum, dp))


# @lc code=end


#
# @lcpr case=start
# "abc"\n
# @lcpr case=end

# @lcpr case=start
# "aaaaa"\n
# @lcpr case=end

#
