#
# @lc app=leetcode.cn id=377 lang=python3
# @lcpr version=30112
#
# [377] 组合总和 Ⅳ
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]

        # @lc code=end

        #
        # @lcpr case=start
        # [1,2,3]\n4\n
        # @lcpr case=end

        # @lcpr case=start
        # [9]\n3\n
        # @lcpr case=end

        #
