#
# @lc app=leetcode.cn id=2609 lang=python3
# @lcpr version=30105
#
# [2609] 最长平衡子字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        idx, ans = 0, 0
        while(idx < len(s)):
            a, b = 0, 0
            while(idx < len(s) and s[idx] == "0"):
                a, idx = a+1, idx+1
            while(idx < len(s) and s[idx] == "1"):
                b, idx = b+1, idx+1
            ans = max(ans, min(a, b)*2)
        return ans

# @lc code=end

#
# @lcpr case=start
# "01000111"\n
# @lcpr case=end

# @lcpr case=start
# "00111"\n
# @lcpr case=end

# @lcpr case=start
# "111"\n
# @lcpr case=end

#
