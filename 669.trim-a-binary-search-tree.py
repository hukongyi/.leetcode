#
# @lc app=leetcode.cn id=669 lang=python3
# @lcpr version=30112
#
# [669] 修剪二叉搜索树
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        root.right = self.trimBST(root.right,low,high)
        root.left = self.trimBST(root.left,low,high)

        if root.val < low:
            return root.right
        if root.val>high:
            return root.left
        return root


# @lc code=end



#
# @lcpr case=start
# [1,0,2]\n1\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,0,4,null,2,null,null,1]\n1\n3\n
# @lcpr case=end

#

