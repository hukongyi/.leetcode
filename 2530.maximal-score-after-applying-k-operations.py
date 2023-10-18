#
# @lc app=leetcode.cn id=2530 lang=python3
# @lcpr version=30102
#
# [2530] 执行 K 次操作后的最大分数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:

    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            ans -= heapq.heapreplace(nums, nums[0] // 3)
        return ans


# @lc code=end


#
# @lcpr case=start
# [10,10,10,10,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,3,3]\n3\n
# @lcpr case=end

#
