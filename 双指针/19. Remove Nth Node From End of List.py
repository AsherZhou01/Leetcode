# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def findNthFromEnd(start, n):
            fast = start
            slow = start
            # 让 fast 先走 n 步
            for i in range(n):
                fast = fast.next
            # 当 fast 走到链表末尾时，slow 指向的即为倒数第 n 个节点
            while fast:
                slow = slow.next
                fast = fast.next
            return slow
        
        dummy = ListNode(-1)
        dummy.next = head
        # 找到倒数第 n+1 个节点
        prev_node = findNthFromEnd(dummy, n + 1)
        
        # 如果存在，则移除倒数第 n 个节点
        if prev_node and prev_node.next:
            prev_node.next = prev_node.next.next
        
        return dummy.next

    
        