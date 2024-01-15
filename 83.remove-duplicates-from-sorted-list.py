#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30112
#
# [83] 删除排序链表中的重复元素
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        pre = head
        cur = pre.next
        while cur is not None:
            if cur.val != pre.val:
                pre.next = cur
                pre = pre.next
                cur = cur.next
            else:
                cur = cur.next
        pre.next = None
        return head


# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#
