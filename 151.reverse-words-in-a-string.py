#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30105
#
# [151] 反转字符串中的单词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s[::-1]
        s = ' '.join(word[::-1] for word in s.split())
        return s
# @lc code=end

#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#
