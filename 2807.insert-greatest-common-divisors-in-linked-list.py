#
# @lc app=leetcode.cn id=2807 lang=python3
# @lcpr version=30112
#
# [2807] 在链表中插入最大公约数
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
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head:
            return head
        pre = head
        cur = head.next

        def getGCD(nums1, nums2):
            GCD = min(nums1, nums2)
            while 1:
                if nums1 % GCD == 0 and nums2 % GCD == 0:
                    return GCD
                else:
                    GCD -= 1

        while cur:
            GCD = getGCD(pre.val, cur.val)
            pre.next = ListNode(GCD, cur)
            pre = cur
            cur = cur.next
        return head


# @lc code=end


#
# @lcpr case=start
# [18,6,10,3]\n
# @lcpr case=end

# @lcpr case=start
# [7]\n
# @lcpr case=end

#
