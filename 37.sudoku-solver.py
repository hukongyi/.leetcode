#
# @lc app=leetcode.cn id=37 lang=python3
# @lcpr version=30112
#
# [37] 解数独
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        empytCount = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empytCount != 1

        def dfs(row, line):
            if empytCount == 0:
                return
            for i in range(line, 9):
                if board[row][i] == '.':
                    board[]

# @lc code=end

#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
