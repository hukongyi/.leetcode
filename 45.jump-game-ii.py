#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30112
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10000] * n
        dp[0] = 0
        for i in range(n):
            if dp[i] != 10000:
                for j in range(nums[i]):
                    if i + j + 1 < n:
                        dp[i + j + 1] = min(dp[i + j + 1], dp[i] + 1)
        return dp[-1]


# @lc code=end


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#
