#
# @lc app=leetcode.cn id=513 lang=python3
# @lcpr version=30112
#
# [513] 找树左下角的值
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
from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        while(que):
            n = len(que)
            tmp = []
            for _ in range(n):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return tmp[0]
# @lc code=end


#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,5,6,null,null,7]\n
# @lcpr case=end

#
