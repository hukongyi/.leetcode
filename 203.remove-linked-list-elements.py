#
# @lc app=leetcode.cn id=203 lang=python3
# @lcpr version=30105
#
# [203] 移除链表元素
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        begin = dummy
        while(head):
            if head.val != val:
                begin.next = head
                begin = begin.next
            head = head.next
        begin.next = None
        return dummy.next

# @lc code=end


#
# @lcpr case=start
# [1,2,6,3,4,5,6]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n1\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7]\n7\n
# @lcpr case=end

#
