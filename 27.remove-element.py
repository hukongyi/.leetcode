#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30102
#
# [27] 移除元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

