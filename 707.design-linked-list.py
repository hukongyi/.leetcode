#
# @lc app=leetcode.cn id=707 lang=python3
# @lcpr version=30105
#
# [707] 设计链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.len = 0
        self.head = ListNode()

    def get(self, index: int) -> int:
        if index > self.len-1:
            return -1
        else:
            head = self.head.next
            for _ in range(index):
                head = head.next
            return head.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val, self.head.next)
        self.head.next = new
        self.len += 1

    def addAtTail(self, val: int) -> None:
        head = self.head
        for _ in range(self.len):
            head = head.next
        head.next = ListNode(val)
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        head = self.head
        for _ in range(index):
            head = head.next
        head.next = ListNode(val, head.next)
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.len-1:
            return
        head = self.head
        for _ in range(index):
            head = head.next
        head.next = head.next.next
        self.len -= 1
        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)
        # @lc code=end
