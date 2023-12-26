#
# @lc app=leetcode.cn id=110 lang=python3
# @lcpr version=30112
#
# [110] 平衡二叉树
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            leftHeight = height(node.left)
            if leftHeight == -1:
                return -1
            rightHeight = height(node.right)
            if rightHeight == -1:
                return -1
            if abs(rightHeight-leftHeight) > 1:
                return -1
            return max(leftHeight, rightHeight)+1
        return height(root) >= 0
# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
