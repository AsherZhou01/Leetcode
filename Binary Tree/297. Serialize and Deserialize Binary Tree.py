# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    SEP = ","
    NULL = "#"
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        parts = []
        self.serialize_helper(root, parts)
        return self.SEP.join(parts)

    def serialize_helper(self, root, parts):
        if root is None:
            parts.append(self.NULL)
            return

        # 前序位置
        parts.append(str(root.val))
        self.serialize_helper(root.left, parts)
        self.serialize_helper(root.right, parts)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 将字符串转化成列表，使用deque提高pop的效率
        nodes = deque(data.split(self.SEP))
        return self.deserialize_helper(nodes)

    def deserialize_helper(self, nodes):
        if not nodes:
            return None

        # 前序位置
        # 列表最左侧就是根节点
        first = nodes.popleft()
        if first == self.NULL:
            return None
        
        root = TreeNode(int(first))
        # 这里的nodes是同一个，利用的就是nodes的顺序来填充。不用回溯
        root.left = self.deserialize_helper(nodes)
        root.right = self.deserialize_helper(nodes)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))