#
# @lc app=leetcode.cn id=47 lang=python3
# @lcpr version=30112
#
# [47] 全排列 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        rst = list()

        def dfs(used):
            if len(ans) == len(nums):
                rst.append(ans[:])
                return
            used2 = set()
            for i in range(len(nums)):
                if i not in used and nums[i] not in used2:
                    used.add(i)
                    used2.add(nums[i])
                    ans.append(nums[i])
                    dfs(used)
                    ans.pop()
                    used.remove(i)
        dfs(set())
        return rst
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

