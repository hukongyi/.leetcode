#
# @lc app=leetcode.cn id=367 lang=python3
# @lcpr version=30102
#
# [367] 有效的完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while(l < r):
            mid = l+(r-l)//2
            if mid*mid < num:
                l = mid+1
            else:
                r = mid
        return r*r == num

# @lc code=end


#
# @lcpr case=start
# 16\n
# @lcpr case=end

# @lcpr case=start
# 14\n
# @lcpr case=end

#
