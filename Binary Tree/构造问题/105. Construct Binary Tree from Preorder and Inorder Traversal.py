# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd):
    # 终止条件：如果当前子数组的长度为零，返回 None
        if preStart > preEnd:
            return None

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]

        # rootVal 在中序遍历数组中的索引
        index = 0
        # 在中序遍历中找到 rootVal 的索引
        # 优化：# 定义一个全局变量存储 inorder 中值到索引的映射 valToIndex = {} ------------>
        for i in range(inStart, inEnd + 1):
            if inorder[i] == rootVal:
                index = i
                break

        # 计算左子树中的节点数
        leftSize = index - inStart

        root = TreeNode(rootVal)
        # 递归构造左子树
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                            inorder, inStart, index - 1)

        # 递归构造右子树
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd)

        return root

            