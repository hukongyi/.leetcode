#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30112
#
# [78] 子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = list()

        def drawbacking(nums, index, path):
            ans.append(path[:])
            if len(path) == len(nums):
                return
            for i in range(index, len(nums)):
                path.append(nums[i])
                drawbacking(nums, i+1, path)
                path.pop()

        drawbacking(nums, 0, [])
        return ans
# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
