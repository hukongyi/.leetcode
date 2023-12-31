#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30112
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        l_inorder = inorder[:inorder.index(preorder[0])]
        r_inorder = inorder[inorder.index(preorder[0])+1:]
        l_preorder = preorder[1:1+len(l_inorder)]
        r_preorder = preorder[1+len(l_inorder):]
        if l_inorder:
            root.left = self.buildTree(l_preorder,l_inorder)
        if r_inorder:
            root.right = self.buildTree(r_preorder,r_inorder)
        return root

# @lc code=end


#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#
