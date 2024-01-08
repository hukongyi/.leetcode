#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30113
#
# [200] 岛屿数量
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        flag = [[0] * len(grid) for _ in grid[0]]


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
