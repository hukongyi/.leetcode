#
# @lc app=leetcode.cn id=474 lang=python3
# @lcpr version=30112
#
# [474] 一和零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 创建二维动态规划数组，初始化为0
        for s in strs:  # 遍历物品
            zeroNum = s.count('0')  # 统计0的个数
            oneNum = len(s) - zeroNum  # 统计1的个数
            for i in range(m, zeroNum - 1, -1):  # 遍历背包容量且从后向前遍历
                for j in range(n, oneNum - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroNum][j - oneNum] + 1)  # 状态转移方程
        return dp[m][n]

# @lc code=end


#
# @lcpr case=start
# ["10", "0001", "111001", "1", "0"]\n5\n3\n
# @lcpr case=end

# @lcpr case=start
# ["10", "0", "1"]\n1\n1\n
# @lcpr case=end

#
