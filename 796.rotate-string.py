#
# @lc app=leetcode.cn id=796 lang=python3
# @lcpr version=30102
#
# [796] 旋转字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s
# @lc code=end


#
# @lcpr case=start
# "abcde"\n"cdeab"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"abced"\n
# @lcpr case=end

#
