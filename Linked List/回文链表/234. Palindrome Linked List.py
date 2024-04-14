# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # 左侧指针
    left = None

    def isPalindrome(self, head):
        global left
        left = head
        return self.traverse(head)

    def traverse(self, right):
        global left
        if right is None:
            return True
        res = self.traverse(right.next)
        # 后序遍历代码
        # in diff level => diff right node
        res = res and (right.val == left.val)
        # update left and try to match right at next level
        left = left.next
        return res
        