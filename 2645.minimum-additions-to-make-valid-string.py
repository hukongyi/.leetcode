#
# @lc app=leetcode.cn id=2645 lang=python3
# @lcpr version=30112
#
# [2645] 构造有效字符串的最少插入数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def addMinimum(self, word: str) -> int:
        ans = list()
        count = 0
        next = {"a": "b", "b": "c", "c": "a"}
        i = 0
        while i < len(word):
            if len(ans) == 0:
                if word[i] != "a":
                    ans.append("a")
                    count += 1
                else:
                    ans.append(word[i])
                    i += 1
            else:
                if word[i] == next[ans[-1]]:
                    ans.append(word[i])
                    i += 1
                else:
                    ans.append(next[ans[-1]])
                    count += 1
        count += ord("c") - ord(ans[-1])
        return count


# @lc code=end


#
# @lcpr case=start
# "b"\n
# @lcpr case=end

# @lcpr case=start
# "aaa"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#
