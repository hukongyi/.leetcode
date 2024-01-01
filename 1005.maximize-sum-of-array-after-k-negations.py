#
# @lc app=leetcode.cn id=1005 lang=python3
# @lcpr version=30112
#
# [1005] K 次取反后最大化的数组和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        def reverse(nums):
            min_num = float("inf")
            min_i = 0
            for i in range(len(nums)):
                if nums[i] < min_num:
                    min_num = nums[i]
                    min_i = i
            nums[min_i] = -nums[min_i]

        for i in range(k):
            reverse(nums)
        return sum(nums)


# @lc code=end


#
# @lcpr case=start
# [4,2,3]\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,-1,0,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,-3,-1,5,-4]\n2\n
# @lcpr case=end

#
