#
# @lc app=leetcode.cn id=541 lang=python3
# @lcpr version=30105
#
# [541] 反转字符串 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        s = list(s)
        n = len(s)//(2*k)
        for i in range(n):
            for j in range(k//2):
                s[j+i*2*k], s[k-j-1+i*2*k] = s[k-j-1+i*2*k], s[j+i*2*k]
        i = n
        k2 = min(k, len(s)-n*2*k)
        for j in range(k2//2):
            s[j+i*2*k], s[k2-j-1+i*2*k] = s[k2-j-1+i*2*k], s[j+i*2*k]
        return ''.join(s)

# @lc code=end


#
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

# @lcpr case=start
# "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"\n39\n
# @lcpr case=end
#