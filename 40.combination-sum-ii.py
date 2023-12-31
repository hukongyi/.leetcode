#
# @lc app=leetcode.cn id=40 lang=python3
# @lcpr version=30112
#
# [40] 组合总和 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def drawbacking(self, candidates, target, index, path, ans,):
        if sum(path) == target:
            ans.append(path.copy())
            return
        if sum(path) > target:
            return
        for i in range(index, len(candidates)):
            if i == index or candidates[i] != candidates[i-1]:
                path.append(candidates[i])
                self.drawbacking(candidates, target, i+1, path, ans)
                path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = list()
        self.drawbacking(candidates, target, 0, [], ans)
        return ans
        # @lc code=end

        #
        # @lcpr case=start
        # [10,1,2,7,6,1,5]\n8\n
        # @lcpr case=end

        # @lcpr case=start
        # [2,5,2,1,2]\n5\n
        # @lcpr case=end

        #
