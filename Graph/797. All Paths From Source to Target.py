class Solution(object):
    def __init__(self):
        # 记录所有路径
        self.res = []
    def allPathsSourceTarget(self, graph):
        # 维护递归过程中经过的路径
        path = []
        self.traverse(graph, 0, path)
        return self.res
    # 图的遍历框架
    def traverse(self, graph, s, path):
        # 添加节点 s 到路径
        path.append(s)
        n = len(graph)
        if s == n - 1:
            # 到达终点
            self.res.append(path[:])
        # 递归每个相邻节点
        for v in graph[s]:
            self.traverse(graph, v, path)
        # 从路径移出节点 s
        path.pop()
        