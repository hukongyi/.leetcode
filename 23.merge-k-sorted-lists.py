#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30112
#
# [23] 合并 K 个升序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

ListNode.__lt__ = lambda a, b: a.val < b.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        p = [i for i in lists if i]
        heapq.heapify(p)
        dummy = ListNode()
        cur = dummy
        while p:
            cur.next = heapq.heappop(p)
            cur = cur.next
            if cur.next is not None:
                heapq.heappush(p, cur.next)
        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#
