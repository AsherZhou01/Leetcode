# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    successor = None # 后继节点
    # 反转以 head 为起点的 n 个节点，返回新的头节点
    def reverseN(self, head, n):
        global successor
        if n == 1:
            # 记录第 n + 1 个节点
            successor = head.next
            return head
        # 以 head.next 为起点，需要反转前 n - 1 个节点
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        # 让反转之后的 head 节点和后面的节点连起来
        # ???
        head.next = successor
        return last 

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # base case
        if left == 1:
            return self.reverseN(head, right)
        # 前进到反转的起点触发 base case
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
        