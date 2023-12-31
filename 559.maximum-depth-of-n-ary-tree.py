#
# @lc app=leetcode.cn id=559 lang=python3
# @lcpr version=30112
#
# [559] N 叉树的最大深度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        que = deque([root])
        level = 0
        while que:
            level += 1
            for _ in range(len(que)):
                node = que.popleft()
                for child in node.children:
                    que.append(child)
        return level

# @lc code=end

#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#
