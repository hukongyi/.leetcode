#
# @lc app=leetcode.cn id=2316 lang=python3
# @lcpr version=30102
#
# [2316] 统计无向图中无法互相到达点对数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import math


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        res = 0
        for i in range(n):
            res += n-uf.getSize(uf.find(i))
        return res//2


class UnionFind:
    def __init__(self, n) -> None:
        self.paranets = list(range(n))
        self.sizes = [1]*n

    def find(self, x) -> int:
        if self.paranets[x] == x:
            return x
        else:
            self.paranets[x] = self.find(self.paranets[x])
            return self.paranets[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.sizes[rx] > self.sizes[ry]:
                self.paranets[ry] = rx
                self.sizes[rx] += self.sizes[ry]
            else:
                self.paranets[rx] = ry
                self.sizes[ry] += self.sizes[rx]

    def getSize(self, x):
        return self.sizes[x]


# @lc code=end


#
# @lcpr case=start
# 3\n[[0,1],[0,2],[1,2]]\n
# @lcpr case=end

# @lcpr case=start
# 7\n[[0,2],[0,5],[2,4],[1,6],[5,4]]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]\n
# @lcpr case=end
#
