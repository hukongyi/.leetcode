#
# @lc app=leetcode.cn id=701 lang=python3
# @lcpr version=30112
#
# [701] 二叉搜索树中的插入操作
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
           return TreeNode(val)
        pre = None
        cur = root
        while cur:
            pre = cur
            if cur.val>val:
                cur = cur.left
            else:
                cur = cur.right
        if pre.val>val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return root
# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [40,20,60,10,30,50,70]\n25\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3,null,null,null,null,null,null]\n5\n
# @lcpr case=end

#

