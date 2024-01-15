#
# @lc app=leetcode.cn id=2696 lang=python3
# @lcpr version=30112
#
# [2696] 删除子串后的字符串最小长度
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        ans = list()
        for i in range(len(s)):
            if ans and (
                (ans[-1] == "A" and s[i] == "B") or (ans[-1] == "C" and s[i] == "D")
            ):
                ans.pop()
            else:
                ans.append(s[i])
        return len(ans)


# @lc code=end


#
# @lcpr case=start
# "ABFCACDB"\n
# @lcpr case=end

# @lcpr case=start
# "ACBBD"\n
# @lcpr case=end

#
