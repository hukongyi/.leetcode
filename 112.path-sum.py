#
# @lc app=leetcode.cn id=112 lang=python3
# @lcpr version=30112
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def getSum(node, Nsum):
            if node is None:
                return False
            Nsum += node.val
            if node.left is None and node.right is None:
                return Nsum == targetSum
            return (getSum(node.left, Nsum) or getSum(node.right, Nsum))
        return getSum(root, 0)

# @lc code=end


#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
