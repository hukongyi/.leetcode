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
        def bfs(i, j):
            q = [[i, j]]
            dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            while q:
                x, y = q.pop(0)
                for dx, dy in dxy:
                    x_new = x + dx
                    y_new = y + dy
                    if (
                        x_new >= 0
                        and y_new >= 0
                        and x_new < len(grid)
                        and y_new < len(grid[0])
                    ):
                        if flag[x_new][y_new] == 0 and grid[x_new][y_new] == "1":
                            flag[x_new][y_new] = 1
                            q.append([x_new, y_new])

        flag = [[0] * len(grid[0]) for _ in grid]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if flag[i][j] == 0 and grid[i][j] == "1":
                    flag[i][j] = 1
                    count += 1
                    bfs(i, j)
        return count


# @lc code=end


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
