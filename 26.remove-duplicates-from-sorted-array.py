 #
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30102
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

