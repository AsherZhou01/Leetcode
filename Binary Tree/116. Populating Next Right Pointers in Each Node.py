# traverse的方法

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        # 遍历「三叉树」，连接相邻节点
        self.traverse(root.left, root.right)
        return root

    # 三叉树遍历框架
    def traverse(self, node1, node2):
        if node1 is None or node2 is None:
            return
        # 将传入的两个节点穿起来
        node1.next = node2

        # 连接相同父节点的两个子节点
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        # 连接跨越父节点的两个子节点------->
        self.traverse(node1.right, node2.left)
        