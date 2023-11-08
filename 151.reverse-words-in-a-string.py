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
        slen = 0
        s = list(s)
        l = 0
        r = 0
        while(r < len(s)):
            while(l < len(s) and s[l] == ' '):
                l += 1
                print(l)
            r = l
            while(r < len(s) and s[r] != ' '):
                r += 1
            print(l, r)
            if r == len(s):
                r += 1
            s[slen:slen+r-l] = s[l:r:-1]
            slen += r-l
            l = r
        return ''.join(s[:slen])

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
