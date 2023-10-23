#
# @lc app=leetcode.cn id=766 lang=python3
# @lcpr version=30102
#
# [766] 托普利茨矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1,n):
            for j in range(1,m):
                if matrix[j][i]!=matrix[j-1][i-1]:
                    return False
        return True


# @lc code=end



#
# @lcpr case=start
# [[1,2,3,4],[5,1,2,3],[9,5,1,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,2]]\n
# @lcpr case=end

#

