from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # 使用 deque 初始化队列，并直接将 root 入队
        q = deque([root])
        # root 本身就是一层，depth 初始化为 1
        depth = 1  

        while q:
            size = len(q)
            for i in range(size):
                # 使用 popleft() 从 deque 中取出元素
                cur = q.popleft()  
                # 判断是否到达终点
                if not cur.left and not cur.right:
                    return depth
                # 将 cur 的相邻节点加入队列
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            # 这里增加深度
            depth += 1

        return depth
        