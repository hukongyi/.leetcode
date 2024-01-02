#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30112
#
# [63] 不同路径 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                print(j, i,dp[j][i])
                if obstacleGrid[j][i] == 1:
                    dp[j][i] = 0
                else:
                    if j==0 and i==0:
                        continue
                    elif j != 0 and i != 0:
                        dp[j][i] = dp[j-1][i]+dp[j][i-1]
                    elif j == 0:
                        dp[j][i] = dp[j][i-1]
                    elif i == 0:
                        dp[j][i] = dp[j-1][i]
        return dp[-1][-1]
# @lc code=end


#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0]]\n
# @lcpr case=end
#
