#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30112
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invaertNode(node):
            if node is not None:
                node.left, node.right = node.right, node.left
                invaertNode(node.left)
                invaertNode(node.right)
        invaertNode(root)
        return root
# @lc code=end


#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
