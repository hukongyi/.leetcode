#
# @lc app=leetcode.cn id=617 lang=python3
# @lcpr version=30112
#
# [617] 合并二叉树
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
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            root = root2
        elif root2 is None:
            root = root1
        else:
            root = TreeNode(root1.val+root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        return root

# @lc code=end


#
# @lcpr case=start
# [1,3,2,5]\n[2,1,3,null,4,null,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n[1,2]\n
# @lcpr case=end

#
