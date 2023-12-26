#
# @lc app=leetcode.cn id=116 lang=python3
# @lcpr version=30112
#
# [116] 填充每个节点的下一个右侧节点指针
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        que = deque([root])
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if i != n-1:
                    node.next = que[0]
                if node.left is not None:
                    que.append(node.left)
                    que.append(node.right)
        return root


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
