# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break 
        # two circumstances for jumping out of while loop: 
        # 1. fast/fast.next is None 2. fast == slow
        if not fast or not fast.next:
            return None
        # set either slow or fast to head works
        # the key is that the distance from head to the cycles's start point equals to 
        # the distance from meet point to the start point + n * cycles's distance
        slow = head 
        # forward at the same speed
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow
        