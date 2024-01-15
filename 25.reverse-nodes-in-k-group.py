#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30112
#
# [25] K 个一组翻转链表
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pre = head
        node_list = list()
        count = 0
        while pre is not None and count < k:
            count += 1
            node_list.append(pre)
            pre = pre.next
        if count < k:
            return head
        node_list[0].next = self.reverseKGroup(node_list[-1].next, k)
        for i in range(k - 1):
            node_list[i + 1].next = node_list[i]
        return node_list[-1]


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#
