#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30102
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
# @lc code=end

#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

