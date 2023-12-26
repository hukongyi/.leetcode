#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30112
#
# [104] 二叉树的最大深度
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
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        que = deque([root])
        level = 0
        while que:
            level += 1
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if i != n-1:
                    node.next = que[0]
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
        return level
# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#
