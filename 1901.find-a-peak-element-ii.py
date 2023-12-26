#
# @lc app=leetcode.cn id=1901 lang=python3
# @lcpr version=30112
#
# [1901] 寻找峰值 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        low, high = 0, m - 1
        while low <= high:
            i = (low + high) // 2
            j = mat[i].index(max(mat[i]))
            if i - 1 >= 0 and mat[i][j] < mat[i - 1][j]:
                high = i - 1
                continue
            if i + 1 < m and mat[i][j] < mat[i + 1][j]:
                low = i + 1
                continue
            return [i, j]
        return None # impossible
            # @lc code=end

            #
            # @lcpr case=start
            # [[1,4],[3,2]]\n
            # @lcpr case=end

            # @lcpr case=start
            # [[10,20,15],[21,30,14],[7,16,32]]\n
            # @lcpr case=end

            #
