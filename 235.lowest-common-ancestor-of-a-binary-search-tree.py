#
# @lc app=leetcode.cn id=235 lang=python3
# @lcpr version=30112
#
# [235] 二叉搜索树的最近公共祖先
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
# @lc code=end


#
# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n8\n
# @lcpr case=end

# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n4\n
# @lcpr case=end

#
