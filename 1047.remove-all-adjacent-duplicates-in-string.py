#
# @lc app=leetcode.cn id=1047 lang=python3
# @lcpr version=30112
#
# [1047] 删除字符串中的所有相邻重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if not stack or stack[-1] != item:
                stack.append(item)
            else:
                stack.pop()
        return ''.join(stack)
# @lc code=end


#
# @lcpr case=start
# "abbaca"\n
# @lcpr case=end

#
