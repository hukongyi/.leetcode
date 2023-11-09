#
# @lc app=leetcode.cn id=2258 lang=python3
# @lcpr version=30106
#
# [2258] 逃离火灾
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(q):
            time = [[-1]*n for _ in range(m)]
            for i, j in q:
                time[i][j] = 0
            t = 1
            while q:
                tmp = q
                q = []
                for i, j in tmp:
                    for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0 and time[x][y] < 0:
                            time[x][y] = t
                            q.append((x, y))
                t += 1
            return time[-1][-1], time[-1][-2], time[-2][-1]

        man_to_house, m1, m2 = bfs([(0, 0)])
        if man_to_house == -1:
            return -1
        fire_pos = [(i, j) for i, row in enumerate(grid)
                    for j, x in enumerate(row) if x == 1]
        fire_to_house, f1, f2 = bfs(fire_pos)
        if fire_to_house == -1:
            return int(1e9)
        
        d = fire_to_house-man_to_house
        if d<0:
            return -1
        print(man_to_house,fire_to_house,d)
        if m1!=-1 and m1+d<f1 or m2!=-1 and m2+d<f2:
            return d
        return d-1
# @lc code=end


#
# @lcpr case=start
# [[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,0],[0,1,2,0],[0,2,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[2,2,0],[1,2,0]]\n
# @lcpr case=end

#
