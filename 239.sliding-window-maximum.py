#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30112
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())
        return result
        # @lc code=end

        #
        # @lcpr case=start
        # [1,3,-1,-3,5,3,6,7]\n3\n
        # @lcpr case=end

        # @lcpr case=start
        # [1]\n1\n
        # @lcpr case=end

        #
