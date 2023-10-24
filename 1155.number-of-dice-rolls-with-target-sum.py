#
# @lc app=leetcode.cn id=1155 lang=python3
# @lcpr version=30102
#
# [1155] 掷骰子等于目标和的方法数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n:
            return 0
        old = [0]*target
        new = [0]*target
        for i in range(min(k, target)):
            old[i] = 1
        for i in range(1, n):
            for j in range(i, target):
                new[j] = sum(old[max(0, j-k):j]) % (10**9 + 7)
            for j in range(i):
                new[j] = 0
            old, new = new, old
        return old[-1]
# @lc code=end


#
# @lcpr case=start
# 1\n6\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n6\n10\n
# @lcpr case=end

# @lcpr case=start
# 30\n30\n32\n
# @lcpr case=end

#
