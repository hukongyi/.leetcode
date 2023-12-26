#
# @lc app=leetcode.cn id=145 lang=python3
# @lcpr version=30112
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traversal(node):
            if node is not None:
                traversal(node.left)
                traversal(node.right)
                ans.append(node.val)
        traversal(root)
        return ans
# @lc code=end


#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
