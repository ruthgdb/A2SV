class OrderedStream:

    def __init__(self, n: int):
        self.d={}
        self.ptr=1

    def insert(self, idkey: int, value: str) -> List[str]:
        self.d[idkey]=value 
        result=[]

        while self.ptr in self.d:
            result.append(self.d[self.ptr])
            self.ptr+=1 

        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)