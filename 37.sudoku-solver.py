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
        self.empytCount = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    self.empytCount += 1

        def is_valid(row, col, num):
            # Check the row and column
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False

            # Check the 3x3 subgrid
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[startRow + i][startCol + j] == num:
                        return False
            return True

        def dfs(row, line):
            if self.empytCount == 0:
                return True
            if board[row][line] == ".":
                for num in "123456789":
                    if is_valid(row, line, num):
                        board[row][line] = num
                        self.empytCount -= 1
                        finish = dfs(row + (line + 1) // 9, (line + 1) % 9)
                        if finish:
                            return True
                        board[row][line] = "."
                        self.empytCount += 1

            else:
                finish = dfs(row + (line + 1) // 9, (line + 1) % 9)
                if finish:
                    return True

        dfs(0, 0)


# @lc code=end

#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#
