#
# @lc app=leetcode.cn id=216 lang=python3
# @lcpr version=30112
#
# [216] 组合总和 III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = list()

        def drawbacking(k, n, path, index, ans):
            if sum(path) > n or len(path) > k:
                return
            if sum(path) == n and len(path) == k:
                ans.append(path.copy())
                return
            for i in range(index, 10):
                path.append(i)
                drawbacking(k, n, path, i+1, ans)
                path.pop()
        drawbacking(k, n, [], 1, ans)
        return ans
        # @lc code=end

        #
        # @lcpr case=start
        # 3\n7\n
        # @lcpr case=end

        # @lcpr case=start
        # 3\n9\n
        # @lcpr case=end

        # @lcpr case=start
        # 4\n1\n
        # @lcpr case=end

        #
