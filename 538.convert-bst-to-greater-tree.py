#
# @lc app=leetcode.cn id=538 lang=python3
# @lcpr version=30112
#
# [538] 把二叉搜索树转换为累加树
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
    def __init__(self):
        self.pre = 0
    def Traveal(self,cur):
        if not cur:
            return
        self.Traveal(cur.right)
        cur.val += self.pre
        self.pre = cur.val
        self.Traveal(cur.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.Traveal(root)
        return root

# @lc code=end



#
# @lcpr case=start
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end

# @lcpr case=start
# [0,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4,1]\n
# @lcpr case=end

#

