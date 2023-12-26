#
# @lc app=leetcode.cn id=404 lang=python3
# @lcpr version=30112
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def getLeft(node, ifleft):
            if node is None:
                return 0
            if node.left is None and node.right is None and ifleft == 1:
                return node.val
            return getLeft(node.left, 1)+getLeft(node.right, 0)
        return getLeft(root, 0)

# @lc code=end


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
