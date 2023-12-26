#
# @lc app=leetcode.cn id=429 lang=python3
# @lcpr version=30112
#
# [429] N 叉树的层序遍历
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        que = deque([root])
        result = []
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.children:
                    for child in node.children:
                        que.append(child)
            result.append(tmp)
        return result
        
# @lc code=end



#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#

