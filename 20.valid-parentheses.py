#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30112
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            else:
                if not stack or stack.pop() != item:
                    return False
        return True if not stack else False
# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#
