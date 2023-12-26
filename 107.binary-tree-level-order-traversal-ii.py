#
# @lc app=leetcode.cn id=107 lang=python3
# @lcpr version=30112
#
# [107] 二叉树的层序遍历 II
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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        que = deque([root])
        result = []
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            result.append(tmp)
        return result[::-1]
# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
