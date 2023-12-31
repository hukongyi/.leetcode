#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30112
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        rst = list()

        def dfs(used):
            if len(ans) == len(nums):
                rst.append(ans[:])
                return
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])
                    ans.append(nums[i])
                    dfs(used)
                    ans.pop()
                    used.remove(nums[i])
        dfs(set())
        return rst
# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
