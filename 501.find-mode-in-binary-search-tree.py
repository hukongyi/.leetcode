#
# @lc app=leetcode.cn id=501 lang=python3
# @lcpr version=30112
#
# [501] 二叉搜索树中的众数
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.pre = None
        self.ans = list()
        self.countMax = 0
        self.count = 0

        def searchBST(node):
            if node is None:
                return
            searchBST(node.left)
            if self.pre is not None:
                print(node.val)
                if self.pre.val == node.val:
                    self.count += 1
                else:
                    self.count=1
                if self.count == self.countMax:
                    self.ans.append(node.val)
                elif self.count > self.countMax:
                    print(self.count, self.countMax)
                    self.ans = list([node.val])
                    self.countMax = self.count
            else:
                self.count += 1
                self.ans.append(node.val)
                self.countMax = 1
            self.pre = node
            searchBST(node.right)
        searchBST(root)
        return self.ans

# @lc code=end


#
# @lcpr case=start
# [1,null,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end
#
