#
# @lc app=leetcode.cn id=2735 lang=python3
# @lcpr version=30112
#
# [2735] 收集巧克力
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        cost = sum(nums)
        min_cost_each = nums.copy()
        for i in range(1, len(nums)):
            nums.append(nums.pop(0))
            for j in range(len(nums)):
                min_cost_each[j] = min(min_cost_each[j], nums[j])
            cost = min(sum(min_cost_each)+i*x, cost)
        return cost
# @lc code=end


#
# @lcpr case=start
# [20,1,15]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n4\n
# @lcpr case=end

#
