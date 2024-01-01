#
# @lc app=leetcode.cn id=968 lang=python3
# @lcpr version=30112
#
# [968] 监控二叉树
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return inf, 0, 0  # 空节点不能安装摄像头，也无需被监控到
            l_choose, l_by_fa, l_by_children = dfs(node.left)
            r_choose, r_by_fa, r_by_children = dfs(node.right)
            choose = min(l_choose, l_by_fa) + min(r_choose, r_by_fa) + 1
            by_fa = min(l_choose, l_by_children) + min(r_choose, r_by_children)
            by_children = min(l_choose + r_by_children, l_by_children + r_choose, l_choose + r_choose)
            return choose, by_fa, by_children
        choose, _, by_children = dfs(root)  # 根节点没有父节点
        return min(choose, by_children)
# @lc code=end



#
# @lcpr case=start
# [0,0,null,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,null,0,null,0,null,null,0]\n
# @lcpr case=end

#

