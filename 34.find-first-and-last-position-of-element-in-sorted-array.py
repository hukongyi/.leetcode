# @lcpr-before-debug-begin
from python3problem34 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30102
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def binsearch(self, nums, target, l, r, higher):
        ans = r
        while(l <= r):
            mid = l + (r - l) // 2
            print(higher, mid, l, r)
            if (nums[mid] < target) or (higher and (nums[mid] <= target)):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1

        if higher == 0 and ans == 0 and nums[ans] == target:
            return ans-1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        l = self.binsearch(nums, target, 0, len(nums) - 1, 0) + 1
        r = self.binsearch(nums, target, l, len(nums) - 1, 1)
        print(l, r)
        if (l <= r) and (nums[l] == target):
            return [l, r]
        else:
            return [-1, -1]
# @lc code=end


# 2
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2]\n2\n
# @lcpr case=end

#
