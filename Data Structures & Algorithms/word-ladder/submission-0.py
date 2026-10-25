class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        

        adj_list = collections.defaultdict(list)
        wordList.append(beginWord)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j + 1:]
                adj_list[pattern].append(w)

        visited = set([beginWord])

        res = 1

        queue = collections.deque([beginWord])

        while queue:
            
            for i in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return res

                for j in range(len(w)):
                    pattern = w[:j] + '*' + w[j + 1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            res += 1
        return 0
