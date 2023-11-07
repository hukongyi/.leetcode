#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30105
#
# [142] 环形链表 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        step = 0
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            step += 1
            if fast == slow:
                slow = dummy
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

# @lc code=end


#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#
