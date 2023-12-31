#
# @lc app=leetcode.cn id=530 lang=python3
# @lcpr version=30112
#
# [530] 二叉搜索树的最小绝对差
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return float('inf')
        MinimumDifference = float('inf')
        node = root.left
        while node:
            MinimumDifference = min(MinimumDifference, root.val - node.val)
            MinimumDifference = min(
                MinimumDifference, self.getMinimumDifference(node))
            node = node.right
        node = root.right
        while node:
            MinimumDifference = min(MinimumDifference, node.val - root.val)
            MinimumDifference = min(
                MinimumDifference, self.getMinimumDifference(node))
            node = node.left
        return MinimumDifference


# @lc code=end


#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#
