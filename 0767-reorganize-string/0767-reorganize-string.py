class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-count[c], c) for c in count]
        heapify(heap)
        res = []
        
        while heap:
            first_c, first_char = heappop(heap)
            
            if not res or res[-1] != first_char:
                res.append(first_char)
                first_c += 1
            else:
                if not heap:
                    return ''
                
                sec_c, sec_char = heappop(heap)
                res.append(sec_char)
                sec_c += 1
                
                if sec_c < 0:
                    heappush(heap, (sec_c, sec_char))
                    
            if first_c < 0:
                heappush(heap, (first_c, first_char))
                
        return ''.join(res)