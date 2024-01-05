#
# @lc app=leetcode.cn id=2397 lang=python3
# @lcpr version=30112
#
# [2397] 被列覆盖的最多行数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if numSelect == n:
            return m
        s = list()
        self.maxRows = 0

        def getRows():
            rows = 0
            remain = list()
            for j in range(n):
                if j not in s:
                    remain.append(j)
            for i in range(m):
                tmp = 0
                for j in remain:
                    if matrix[i][j] == 1:
                        tmp += 1
                if tmp == 0:
                    rows += 1
            return rows

        def getMaxRows():
            if len(s) == numSelect:
                self.maxRows = max(self.maxRows, getRows())
                return
            for i in range(len(s), n - numSelect + len(s) + 1):
                s.append(i)
                getMaxRows()
                s.pop()

        getMaxRows()
        return self.maxRows


# @lc code=end


#
# @lcpr case=start
# [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n1\n
# @lcpr case=end

#
