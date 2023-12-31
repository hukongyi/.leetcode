#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30112
#
# [51] N 皇后
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = list()
        rst = list()

        def ifOK(ans, line, row):
            for i in range(row):
                if ans[i][line] == 'Q':
                    return False
            i = row-1
            j = line-1
            while i >= 0 and j >= 0:
                if ans[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i = row-1
            j = line+1
            while i >= 0 and j < n:
                if ans[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def dfs(row):
            if len(ans) == n:
                rst.append(ans[:])
                return
            for i in range(n):
                if ifOK(ans, i, row):
                    tmp = ["."]*n
                    tmp[i] = "Q"
                    ans.append(''.join(tmp))
                    dfs(row+1)
                    ans.pop()
        dfs(0)
        return rst
# @lc code=end


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
