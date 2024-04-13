from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # 记录需要跳过的死亡密码
        dead = set(deadends)
        # 如果初始状态就是死亡状态,返回-1
        if '0000' in dead:
            return -1
        
        # 记录已经穷举过的密码,防止走回头路
        visited = set()
        visited.add('0000')
        
        # 初始化BFS队列
        q = deque([('0000', 0)])
        
        while q:
            cur, step = q.popleft()
            # 如果找到目标密码,返回转动步数
            if cur == target:
                return step
            # 一次遍历当前密码的所有可能取值
            for i in range(4):
                up = cur[:i] + str((int(cur[i]) + 1) % 10) + cur[i+1:]
                down = cur[:i] + str((int(cur[i]) - 1) % 10) + cur[i+1:]
                for next_status in [up, down]:
                    if next_status not in dead and next_status not in visited:
                        visited.add(next_status)
                        q.append((next_status, step + 1))
        
        # 无法转动到目标密码
        return -1