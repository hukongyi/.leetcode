#
# @lc app=leetcode.cn id=844 lang=python3
# @lcpr version=30102
#
# [844] 比较含退格的字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
def getresult(s):
    s = list(s)
    slow, fast = 0, 0
    while fast < len(s):
        if s[fast] == "#":
            slow -= 1
        else:
            slow = max(slow, 0)
            s[slow] = s[fast]
            slow += 1
        fast += 1
    return slow, s


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        len_s, s = getresult(s)
        len_t, t = getresult(t)
        return s[:len_s] == t[:len_t]

# @lc code=end



#
# @lcpr case=start
# "ab#c"\n"ad#c"\n
# @lcpr case=end

# @lcpr case=start
# "ab##"\n"c#d#"\n
# @lcpr case=end

# @lcpr case=start
# "a#c"\n"b"\n
# @lcpr case=end

#

