#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30112
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = float('-inf')
        # count=0
        # for i in range(len(nums)):
        #     count+=nums[i]
        #     if count>ans:
        #         ans = count
        #     if count<0:
        #         count=0
        # return ans
        # method2
        dp = [nums[0]]*len(nums)
        for i in range(1,len(nums)): dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

