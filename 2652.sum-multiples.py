#
# @lc app=leetcode.cn id=2652 lang=python3
# @lcpr version=30102
#
# [2652] 倍数求和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getsum(self, n, p):
        a = n//p
        return p*(1+a)*a/2

    def sumOfMultiples(self, n: int) -> int:
        return int(self.getsum(n, 3)+self.getsum(n, 5)+self.getsum(n, 7)-self.getsum(n, 3*5)-self.getsum(n, 3*7)-self.getsum(n, 5*7)+self.getsum(n, 3*5*7))
# @lc code=end


#
# @lcpr case=start
# 7\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 105\n
# @lcpr case=end

#
