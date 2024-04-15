# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        # 利用函数定义，先翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 然后交换左右子节点
        root.left = right
        root.right = left

        # 和定义逻辑自恰：以 root 为根的这棵二叉树已经被翻转，返回 root
        return root
        