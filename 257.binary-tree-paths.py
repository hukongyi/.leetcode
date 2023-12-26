#
# @lc app=leetcode.cn id=257 lang=python3
# @lcpr version=30112
#
# [257] 二叉树的所有路径
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        result = list()
        path = list()

        def traversal(path, node):
            path.append(node.val)
            if not node.left and not node.right:
                result.append('->'.join(map(str, path)))
                return
            if node.left:
                traversal(path, node.left)
                path.pop()
            if node.right:
                traversal(path, node.right)
                path.pop()
        traversal(path, root)
        return result

# @lc code=end

#
# @lcpr case=start
# [1,2,3,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
