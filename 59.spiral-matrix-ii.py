#
# @lc app=leetcode.cn id=59 lang=python3
# @lcpr version=30104
#
# [59] 螺旋矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dirtype = 0
        a1 = 0
        a2 = 0
        for i in range(n*n):
            ans[a1][a2] = i+1
            a1_tmp, a2_tmp = a1+direct[dirtype %
                                       4][0], a2+direct[dirtype % 4][1]
            if a1_tmp > n-1 or a1_tmp < 0 or a2_tmp > n-1 or a2_tmp < 0 or ans[a1_tmp][a2_tmp] != 0:
                dirtype += 1
                a1_tmp, a2_tmp = a1+direct[dirtype %
                                           4][0], a2+direct[dirtype % 4][1]
            a1, a2 = a1_tmp, a2_tmp
        return ans

# @lc code=end


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
