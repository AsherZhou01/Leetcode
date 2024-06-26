import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        dummy = ListNode(-1)
        p = dummy
        pq = []
        # 将每个链表的头节点加入到最小堆中
        for head in lists:
            if head:  # 如果链表非空
                heapq.heappush(pq, (head.val, head))  # 向堆中添加一个二元组

        # 当堆非空时，进行循环
        while pq:
            # 从堆中弹出最小元素，即具有最小值的节点
            _, node = heapq.heappop(pq)
            # 将这个节点接到p的后面
            p.next = node  
            # 将后继节点加入到堆中
            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))  
            p = p.next

        return dummy.next
    


# 优先队列 pq 中的元素个数最多是 k，所以一次 poll 或者 add 方法的时间复杂度是 O(logk)；
# 所有的链表节点都会被加入和弹出 pq，所以算法整体的时间复杂度是 O(Nlogk)，其中 k 是链表的条数，N 是这些链表的节点总数。

