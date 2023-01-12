class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        incoming = defaultdict(int)
        queue = deque()
        visited = set()
        alph = []

        def check(word1, word2):
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if word1[i] in graph[word2[i]]:
                        return False

                    if word2[i] not in graph[word1[i]]:
                        graph[word1[i]].add(word2[i])
                        incoming[word2[i]] += 1
                        incoming[word1[i]] += 0
                        
                    return True

            return len(word1) <= len(word2)

        for word in words:
            for char in word:
                incoming[char]
                
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not check(words[i], words[j]):
                    return ""
                
        for word in incoming:
            if incoming[word] == 0:
                queue.append(word)

        while queue:
            currWord = queue.popleft()
            if currWord in visited:
                return ""

            alph.append(currWord)
            visited.add(currWord)

            for nxtWord in graph[currWord]:
                incoming[nxtWord] -= 1
                if incoming[nxtWord] == 0:
                    queue.append(nxtWord)
        
        return ''.join(alph)
