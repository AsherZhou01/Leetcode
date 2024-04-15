# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        # 记录所有子树以及出现的次数
        self.subTrees = {}
        # 记录重复的子树根节点
        self.res = []

    def findDuplicateSubtrees(self, root):
        self.serialize(root)
        return self.res

    def serialize(self, root):
        if not root:
            return "#"
        # 先算左右子树的序列化结果
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        myself = left + "," + right + "," + str(root.val)

        freq = self.subTrees.get(myself, 0)
        # 多次重复也只会被加入结果集一次
        if freq == 1:
            self.res.append(root)
        # 给子树对应的出现次数加一
        self.subTrees[myself] = freq + 1
        return myself
        