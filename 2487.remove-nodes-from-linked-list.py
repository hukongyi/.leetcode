#
# @lc app=leetcode.cn id=2487 lang=python3
# @lcpr version=30112
#
# [2487] 从链表中移除节点
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        head.next = self.removeNodes(head.next)
        if head.next is not None and head.val<head.next.val:
            return head.next
        else:
            return head
# @lc code=end



#
# @lcpr case=start
# [5,2,13,3,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

#

