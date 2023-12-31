#
# @lc app=leetcode.cn id=654 lang=python3
# @lcpr version=30112
#
# [654] 最大二叉树
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
def get_max_index(nums):
    max_index = 0
    for i in range(len(nums)):
        if nums[i] > nums[max_index]:
            max_index = i
    return max_index


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        max_index = get_max_index(nums)
        root = TreeNode(nums[max_index])
        if nums[:max_index]:
            root.left = self.constructMaximumBinaryTree(nums[:max_index])
        if nums[max_index+1:]:
            root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

# @lc code=end


#
# @lcpr case=start
# [3,2,1,6,0,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

#
