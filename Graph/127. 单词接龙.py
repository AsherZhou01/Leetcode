class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)  # 将单词列表转换为集合，便于快速查找
        if endWord not in wordSet:
            return 0  # 如果目标单词不在单词列表中，直接返回0
        
        queue = deque([beginWord])  # 使用队列实现BFS
        mapping = {beginWord: 1}  # 记录每个单词的路径长度，起始单词路径长度为1

        while queue:
            current_word = queue.popleft()  # 从队列中获取当前处理的单词
            current_length = mapping[current_word]  # 获取到达当前单词的路径长度

            # 尝试改变当前单词的每一个字母
            for i in range(len(current_word)):
                for j in range(26):  # 对于每个可能的字母
                    new_letter = chr(ord('a') + j)
                    if new_letter != current_word[i]:  # 只有在新字母与当前字母不同时才处理
                        new_word = current_word[:i] + new_letter + current_word[i+1:]
                        if new_word == endWord:
                            return current_length + 1  # 如果新单词是目标单词，返回当前路径长度+1
                        if new_word in wordSet and new_word not in mapping:
                            queue.append(new_word)  # 将新单词添加到队列
                            mapping[new_word] = current_length + 1  # 记录新单词的路径长度

        return 0  # 如果队列为空还没找到目标单词，返回0