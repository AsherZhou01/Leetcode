class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = self.buildGraph(numCourses, prerequisites)
        # visited 列表：用来标记每个节点是否被访问过。
        visited = [False] * numCourses
        # onPath 列表：用来标记当前递归路径上的节点，帮助检测循环。
        onPath = [False] * numCourses
        # hasCycle 列表：用来存储一个布尔值，标记图中是否检测到循环
        hasCycle = [False]
        
        def traverse(graph, s):
            # 如果当前节点已经在当前路径 onPath 上, 则意味着有一个环
            if onPath[s]:
                hasCycle[0] = True
            if visited[s] or hasCycle[0]:
                return
            visited[s] = True
            onPath[s] = True
            for t in graph[s]:
                traverse(graph, t)
            onPath[s] = False
        
        for i in range(numCourses):
            if not visited[i]:
                traverse(graph, i)
            # 意味着有环，不需要再继续了
            if hasCycle[0]:
                break
        # True代表着有环，因此要取反代表不能完成这个课程表
        return not hasCycle[0]
    
    # example: prerequisites = [[1,0],[0,1]]
    # [1,0]: from 0 (prerequisites) to 1
    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for from_course, to_course in prerequisites:
            graph[from_course].append(to_course)
        return graph