from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, inorder, postorder):
        # 使用 defaultdict 初始化 inorder 值到索引的映射
        val_to_index = defaultdict(int)
        for i, value in enumerate(inorder):
            val_to_index[value] = i

        # 辅助函数，用于递归构建二叉树
        def build(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None
            # root 节点对应的值就是后序遍历数组的最后一个元素
            rootVal = postorder[postEnd]
            # rootVal 在中序遍历数组中的索引
            index = val_to_index[rootVal]

            root = TreeNode(rootVal)
            # 递归构造左右子树
            root.left = build(inStart, index - 1, postStart, postStart + index - inStart - 1)
            root.right = build(index + 1, inEnd, postStart + index - inStart, postEnd - 1)
            
            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
        