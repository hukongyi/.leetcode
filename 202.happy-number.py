#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30105
#
# [202] 快乐数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getsquart(self, n):
        ans = 0
        while n > 0:
            ans += (n % 10)**2
            n = n//10
        return ans

    def isHappy(self, n: int) -> bool:
        a = set()
        while(n not in a):
            if n == 1:
                return True
            a.add(n)
            n = self.getsquart(n)
        return False
# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#
