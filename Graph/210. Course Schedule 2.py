class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = self.buildGraph(numCourses, prerequisites)
        visited = [0] * numCourses  # 0 - 未访问, 1 - 访问中, 2 - 已访问
        result = []  # 用来存储拓扑排序
        hasCycle = [False]
        
        def traverse(graph, s):
            if visited[s] == 1:  # 访问中发现重访问，说明有环
                hasCycle[0] = True
                return
            if visited[s] == 2:  # 已经访问过，无需重复处理
                return
            visited[s] = 1  # 标记为访问中
            for t in graph[s]:
                traverse(graph, t)
                if hasCycle[0]:  # 如果发现有环，立刻停止处理
                    return
            visited[s] = 2  # 标记为已访问
            result.append(s)  # 后序位置添加，确保所有依赖后处理
        
        for i in range(numCourses):
            if not visited[i]:
                traverse(graph, i)
                if hasCycle[0]:  # 如果发现有环，返回空列表
                    return []
        return result[::-1]  # 反转结果，因为添加是逆拓扑顺序
    
    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for to_course, from_course in prerequisites:
            graph[from_course].append(to_course)  # 确保方向正确，依赖课程先行
        return graph