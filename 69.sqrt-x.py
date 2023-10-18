#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30102
#
# [69] x 的平方根
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # if x <= 2:
        #     return min(x, 1)
        l = 0
        r = x
        while(l < r):
            mid = (l+r)//2
            if mid*mid >= x:
                r = mid
            else:
                l = mid + 1
        if r*r == x:
            return r
        else:
            return r - 1

# @lc code=end

#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end
#
