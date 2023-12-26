#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30112
#
# [199] 二叉树的右视图
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
            result.append(tmp[-1])
        return result


# @lc code=end


#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
