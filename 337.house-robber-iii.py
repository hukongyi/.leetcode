#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30112
#
# [337] 打家劫舍 III
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
    def rob(self, root: Optional[TreeNode]) -> int:
        def getTreeMax(node):
            if node is None:
                return [0,0]
            l0,l1 = getTreeMax(node.left)
            r0,r1 = getTreeMax(node.right)
            n0 = max(l0,l1)+max(r0,r1)
            n1 = l0+r0+node.val
            return [n0,n1]
        return max(getTreeMax(root))
# @lc code=end



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,null,2,null,3]\n
# @lcpr case=end

#

