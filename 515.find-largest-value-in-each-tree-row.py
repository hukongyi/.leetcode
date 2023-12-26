#
# @lc app=leetcode.cn id=515 lang=python3
# @lcpr version=30112
#
# [515] 在每个树行中找最大值
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        que = deque([root])
        result = []
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            result.append(max(tmp))
        return result
# @lc code=end



#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

