#
# @lc app=leetcode.cn id=494 lang=python3
# @lcpr version=30112
#
# [494] 目标和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        numssum = sum(nums)
        if abs(target) > numssum:
            return 0
        dp = [[0]*(numssum*2+1) for _ in range(len(nums))]
        dp[0][numssum+nums[0]] += 1
        dp[0][numssum-nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(len(dp[0])):
                if dp[i-1][j] != 0:
                    dp[i][j-nums[i]] += dp[i-1][j]
                    dp[i][j+nums[i]] += dp[i-1][j]
        return dp[-1][target+numssum]
# @lc code=end


#
# @lcpr case=start
# [1,1,1,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
