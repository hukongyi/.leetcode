#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30112
#
# [72] 编辑距离
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    l = dp[i - 1][j]
                    r = dp[i][j - 1]
                    dp[i][j] = min(l, r, dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "inten"\n"execu"\n
# @lcpr case=end


# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end
#
