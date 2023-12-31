#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30112
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def __init__(self):
        self.num2str = ["abc", "def", "ghi",
                        "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def drawbacking(self, digits, index, path, ans):
        if len(path) == len(digits):
            ans.append("".join(path))
            return
        if len(path) > len(digits):
            return
        for i in self.num2str[int(digits[index])-2]:
            path.append(i)
            self.drawbacking(digits, index+1, path, ans)
            path.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = list()
        self.drawbacking(digits,0,[],ans)
        return ans
# @lc code=end

#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#
