#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30112
#
# [55] 跳跃游戏
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            if dp[i] == 1:
                for j in range(nums[i]):
                    if i + j + 1 < len(nums):
                        if i + j + 1 == len(nums)-1:
                            return True
                        dp[i + j + 1] = 1
        return bool(dp[-1])


# @lc code=end


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#
