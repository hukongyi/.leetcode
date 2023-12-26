#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30112
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        que = deque()
        que.append([root, root])
        while que:
            for _ in range(len(que)):
                node1, node2 = que.popleft()
                if node1.val != node2.val:
                    return False
                if node1.left and node2.right:
                    que.append([node1.left, node2.right])
                elif node1.left or node2.right:
                    return False
                if node1.right and node2.left:
                    que.append([node1.right, node2.left])
                elif node1.right or node2.left:
                    return False
        return True
# @lc code=end


#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#
