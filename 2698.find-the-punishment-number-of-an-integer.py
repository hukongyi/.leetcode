#
# @lc app=leetcode.cn id=2698 lang=python3
# @lcpr version=30102
#
# [2698] 求一个整数的惩罚数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def punishmentNumber(self, n: int) -> int:
        a = [1, 9, 10, 36, 45, 55, 82, 91, 99, 100, 235, 297, 369, 370, 379, 414, 657, 675, 703, 756, 792, 909, 918, 945, 964, 990, 991, 999, 1000]
        ans = 0
        for i in a:
            if i <= n:
                ans += i*i
            else:
                break
        return ans
# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 37\n
# @lcpr case=end

#

