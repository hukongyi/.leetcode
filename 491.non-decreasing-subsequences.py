#
# @lc app=leetcode.cn id=491 lang=python3
# @lcpr version=30112
#
# [491] 递增子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        rst = list()

        def dfs(index):
            if len(ans) >= 2:
                rst.append(ans[:])
            used = set()
            for i in range(index, len(nums)):
                if (len(ans) == 0 or nums[i] >= ans[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    ans.append(nums[i])
                    dfs(i+1)
                    ans.pop()
        dfs(0)
        return rst

# @lc code=end


#
# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,3,2,1]\n
# @lcpr case=end

#
