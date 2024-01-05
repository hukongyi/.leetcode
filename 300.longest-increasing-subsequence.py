#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30112
#
# [300] 最长递增子序列
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# @lc code=end


#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,6,7,9,4,10,5,6]\n
# @lcpr case=end


#
