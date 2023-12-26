#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30112
#
# [150] 逆波兰表达式求值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = list()
        op = ["+", "-", "*", "/"]
        for item in tokens:
            if item in op:
                num1 = ans.pop()
                num2 = ans.pop()
                if item == '+':
                    ans.append(num1+num2)
                if item == '-':
                    ans.append(num2-num1)
                if item == '*':
                    ans.append(num1*num2)
                if item == '/':
                    print(num2, num1)
                    ans.append(int(num2/num1))
            else:
                ans.append(int(item))
        return ans[0]
# @lc code=end


#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#
