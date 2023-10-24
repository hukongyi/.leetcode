from typing import List
#
# @lc app=leetcode.cn id=977 lang=python3
# @lcpr version=30102
#
# [977] 有序数组的平方
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        l = 0
        r = len(nums)-1
        for i in range(len(nums)):
            if abs(nums[l]) > abs(nums[r]):
                ans[len(nums)-1-i] = nums[l]*nums[l]
                l += 1
            else:
                ans[len(nums)-1-i] = nums[r]*nums[r]
                r -= 1
        return ans

    # @lc code=end

    #
    # @lcpr case=start
    # [-4,-1,0,3,10]\n
    # @lcpr case=end

    # @lcpr case=start
    # [-7,-3,2,3,11]\n
    # @lcpr case=end

    #
