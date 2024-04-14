# 递归方法

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 如果链表为空或者只有一个节点的时候，反转结果就是它自己，直接返回即可
        if not head or not head.next:
            return head
        last = self.reverseList(head.next) 
        # let the return list's end pointing to head
        head.next.next = head 
        # let head points to null
        head.next = None 

        return last