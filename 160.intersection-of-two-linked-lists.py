#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30105
#
# [160] 相交链表
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        tmpA = headA
        tmpB = headB
        while(tmpA):
            lenA += 1
            tmpA = tmpA.next
        while(tmpB):
            lenB += 1
            tmpB = tmpB.next
        if(lenA > lenB):
            for _ in range(lenA-lenB):
                headA = headA.next
        else:
            for _ in range(lenB-lenA):
                headB = headB.next
        while(headA):
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

# @lc code=end


#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#
