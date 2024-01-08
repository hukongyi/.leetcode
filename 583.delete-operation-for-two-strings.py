#
# @lc app=leetcode.cn id=583 lang=python3
# @lcpr version=30112
#
# [583] 两个字符串的删除操作
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            dp[0][i] = i
        for j in range(1, len(word2) + 1):
            dp[j][0] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[j][i] = dp[j - 1][i - 1]
                else:
                    dp[j][i] = min(dp[j - 1][i], dp[j][i - 1]) + 1
        return dp[-1][-1]


# @lc code=end


#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"etco"\n
# @lcpr case=end

#
