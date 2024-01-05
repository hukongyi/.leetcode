#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30112
#
# [1143] 最长公共子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text1) for _ in range(len(text2))]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
        return max(map(max, dp))


# @lc code=end


#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#
