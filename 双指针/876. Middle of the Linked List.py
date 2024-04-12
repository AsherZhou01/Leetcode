# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 快慢指针初始化指向 head
        slow = head
        fast = head
        # 快指针走到末尾时停止
        # 因为只要fast.next而不要判断fast.next.next：即如果链表长度为偶数，也就是说中点有两个的时候，取后面的那个中点
        while fast and fast.next:
            # 慢指针走一步，快指针走两步
            slow = slow.next
            fast = fast.next.next
        # 慢指针指向中点
        return slow