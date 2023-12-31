#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30112
#
# [39] 组合总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def backtracking(self, candidates, target, index,  path, result):
        if sum(path) == target:
            result.append(path.copy())
            return
        if sum(path) > target:
            return
        for i in range(index, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target, i, path, result)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.backtracking(candidates, target, 0, [], result)
        return result
# @lc code=end


#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#
