#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30105
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur1 = head
        pre = dummy
        while(cur1):
            cur2 = cur1.next
            if cur2:
                tmp = cur2.next
                cur2.next = cur1
                cur1.next = tmp
                pre.next = cur2
                pre = cur1
                cur1 = tmp
            else:
                pre.next = cur1
                break
        return dummy.next


# @lc code=end

#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
