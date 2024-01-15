#
# @lc app=leetcode.cn id=2182 lang=python3
# @lcpr version=30112
#
# [2182] 构造限制重复的字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        N = 26
        count = [0] * N
        for c in s:
            count[ord(c) - ord('a')] += 1
        ret = []
        i, j, m = N - 1, N - 2, 0
        while i >= 0 and j >= 0:
            if count[i] == 0: # 当前字符已经填完，填入后面的字符，重置 m
                m, i = 0, i - 1
            elif m < repeatLimit: # 当前字符未超过限制
                count[i] -= 1
                ret.append(chr(ord('a') + i))
                m += 1
            elif j >= i or count[j] == 0: # 当前字符已经超过限制，查找可填入的其他字符
                j -= 1
            else: # 当前字符已经超过限制，填入其他字符，并且重置 m
                count[j] -= 1
                ret.append(chr(ord('a') + j))
                m = 0
        return ''.join(ret)

# @lc code=end



#
# @lcpr case=start
# "cczazcc"\n3\n
# @lcpr case=end

# @lcpr case=start
# "aababab"\n2\n
# @lcpr case=end

#

