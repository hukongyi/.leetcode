#
# @lc app=leetcode.cn id=700 lang=python3
# @lcpr version=30112
#
# [700] 二叉搜索树中的搜索
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

# @lc code=end


#
# @lcpr case=start
# [4,2,7,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

#
