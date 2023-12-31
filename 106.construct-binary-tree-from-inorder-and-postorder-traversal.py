#
# @lc app=leetcode.cn id=106 lang=python3
# @lcpr version=30112
#
# [106] 从中序与后序遍历序列构造二叉树
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder[-1])
        l_inorder = inorder[:inorder.index(postorder[-1])]
        r_inorder = inorder[inorder.index(postorder[-1])+1:]
        l_postorder = postorder[:len(l_inorder)]
        r_postorder = postorder[len(l_inorder):-1]
        if l_inorder:
            root.left = self.buildTree(l_inorder, l_postorder)
        if r_inorder:
            root.right = self.buildTree(r_inorder, r_postorder)
        return root
# @lc code=end


#
# @lcpr case=start
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#
