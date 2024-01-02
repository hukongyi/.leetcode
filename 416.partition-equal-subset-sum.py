#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30112
#
# [416] 分割等和子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum & 1 == 1:
            return False
        half_sum = nums_sum//2
        dp = [[0]*(half_sum+1) for _ in range(len(nums))]
        if nums[0] > half_sum:
            return False
        dp[0][nums[0]] = 1
        for i in range(len(nums)):
            dp[i][0] = 1
        for i in range(1, len(nums)):
            if nums[i] > half_sum:
                return False
            for j in range(half_sum+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i]])
            if dp[i][-1] == 1:
                return True
        return False
# @lc code=end


#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#
