#
# @lc app=leetcode.cn id=222 lang=python3
# @lcpr version=30112
#
# [222] 完全二叉树的节点个数
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left+right+1


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
