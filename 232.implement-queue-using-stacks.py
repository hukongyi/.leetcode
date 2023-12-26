#
# @lc app=leetcode.cn id=232 lang=python3
# @lcpr version=30112
#
# [232] 用栈实现队列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in = list()
        self.stack_out = list()

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        if ans is not None:
            self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)

        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()
        # @lc code=end

        #
        # @lcpr case=start
        # ["MyQueue", "push", "push", "peek", "pop", "empty"][[], [1], [2], [], [], []]\n
        # @lcpr case=end

        #
