#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30105
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    # 定义getNext函数，用于获取next数组
    def getNext(self, next, s):
        j = -1
        next[0] = j
        # 遍历字符串s
        for i in range(1, len(s)):
            # 当j>=0且s[i]不等于s[j+1]时，更新j的值
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            # 当s[i]等于s[j+1]时，j自增1
            if s[i] == s[j+1]:
                j += 1
            # 更新next数组的值
            next[i] = j

    # 定义strStr函数，用于查找needle在haystack中的位置
    def strStr(self, haystack: str, needle: str) -> int:
        # 如果needle为空，返回0
        if not needle:
            return 0
        # 初始化next数组
        next = [0] * len(needle)
        # 调用getNext函数，获取next数组
        self.getNext(next, needle)
        j = -1
        # 遍历haystack
        for i in range(len(haystack)):
            # 当j>=0且haystack[i]不等于needle[j+1]时，更新j的值
            while j >= 0 and haystack[i] != needle[j+1]:
                j = next[j]
            # 当haystack[i]等于needle[j+1]时，j自增1
            if haystack[i] == needle[j+1]:
                j += 1
            # 如果j等于needle的长度减1，返回i减去needle的长度加1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        # 如果没有找到，返回-1
        return -1

# @lc code=end


#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#
