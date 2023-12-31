#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30112
#
# [108] 将有序数组转换为二叉搜索树
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

        # @lc code=end

        #
        # @lcpr case=start
        # [-10,-3,0,5,9]\n
        # @lcpr case=end

        # @lcpr case=start
        # [1,3]\n
        # @lcpr case=end

        #
