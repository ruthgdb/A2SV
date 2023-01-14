class Solution:
    def find(self, node, parents):
        if node == parents[ord(node) - ord('a')]:
            return node
        
        parents[ord(node) - ord('a')] = self.find(parents[ord(node) - ord('a')], parents)
        return parents[ord(node) - ord('a')]
        
    def union(self, u, v, parents, rank):
        pu = self.find(u, parents)
        pv = self.find(v, parents)
        
        if pu != pv:
            parents[ord(pu) - ord('a')] = pv
            
        rank[ord(pv) - ord('a')] = min(u, v, rank[ord(pv) - ord('a')], rank[ord(pu) - ord('a')])
        
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rank = [-1] * 26
        parents = [-1] * 26
        newWord = []
        
        for i in range(26):
            rank[i] = chr(i + 97)
            parents[i] = chr(i + 97)
        
        for i in range(len(s1)):
            self.union(s1[i], s2[i], parents, rank)
            
        for i in range(len(s1)):
            self.find(s1[i], parents)
            self.find(s2[i], parents)
            
        for char in baseStr:
            parent = self.find(char, parents)
            word = rank[ord(parent) - ord('a')]
            newWord.append(word)
            
        return "".join(newWord)