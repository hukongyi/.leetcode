#
# @lc app=leetcode.cn id=100 lang=python3
# @lcpr version=30112
#
# [100] 相同的树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p is None and q is not None) or (p is not None and q is None):
            return False
        que = deque([[p, q]])
        while que:
            nodep, nodeq = que.popleft()
            if nodep and nodeq:
                if nodep.val != nodeq.val:
                    return False
                if nodep.left and nodeq.left:
                    que.append([nodep.left, nodeq.left])
                elif nodep.left or nodeq.left:
                    return False
                if nodep.right and nodeq.right:
                    que.append([nodep.right, nodeq.right])
                elif nodep.right or nodeq.right:
                    return False
        return True
        # @lc code=end

        #
        # @lcpr case=start
        # [1,2,3]\n[1,2,3]\n
        # @lcpr case=end

        # @lcpr case=start
        # [1,2]\n[1,null,2]\n
        # @lcpr case=end

        # @lcpr case=start
        # [1,2,1]\n[1,1,2]\n
        # @lcpr case=end

        #
