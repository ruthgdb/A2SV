class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        res = []
        
        def dfs(flight):
            flights = graph[flight]
            
            while flights:
                next_flight = flights.pop()
                dfs(next_flight)
                
            res.append(flight)

        for frm, to in tickets:
            graph[frm].append(to)

        for _, itinerary in graph.items():
            itinerary.sort(reverse = True)

        dfs('JFK')
        return res[::-1]