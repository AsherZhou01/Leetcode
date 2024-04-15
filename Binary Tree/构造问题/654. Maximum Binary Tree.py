# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        # 找到数组中的最大值和对应的索引
        maxVal = max(nums)
        index = nums.index(maxVal)
        
        # 创建当前的树节点
        root = TreeNode(maxVal)
        # 递归构造左子树和右子树
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        
        return root
        