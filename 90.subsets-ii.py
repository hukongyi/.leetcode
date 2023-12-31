#
# @lc app=leetcode.cn id=90 lang=python3
# @lcpr version=30112
#
# [90] 子集 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        path = []

        def drawbacking(index):
            ans.append(path[:])
            if len(path) == len(nums):
                return
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                drawbacking(i+1)
                path.pop()
        drawbacking(0)
        return ans
# @lc code=end


#
# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
