#
# @lc app=leetcode.cn id=572 lang=python3
# @lcpr version=30112
#
# [572] 另一棵树的子树
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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def ifSame(p, q):
            if (p is None and q is not None) or (p is not None and q is None):
                return False
            que = deque([[p, q]])
            while que:
                nodep, nodeq = que.popleft()
                if nodep and nodeq:
                    if nodep.val != nodeq.val:
                        return False
                    if nodep.left and nodeq.left:
                        que.append([nodep.left, nodeq.left])
                    elif nodep.left or nodeq.left:
                        return False
                    if nodep.right and nodeq.right:
                        que.append([nodep.right, nodeq.right])
                    elif nodep.right or nodeq.right:
                        return False
            return True
        rootque = deque([root])
        while rootque:
            node = rootque.popleft()
            if ifSame(node, subRoot):
                return True
            if node.left:
                rootque.append(node.left)
            if node.right:
                rootque.append(node.right)
        return False

# @lc code=end


#
# @lcpr case=start
# [3,4,5,1,2]\n[4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,2,null,null,null,null,0]\n[4,1,2]\n
# @lcpr case=end

#
