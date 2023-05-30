class MyHashSet:

    def __init__(self):
        self.sets = set()

    def add(self, key: int) -> None:
        self.sets.add(key)

    def remove(self, key: int) -> None:
        if key in self.sets:
            self.sets.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.sets
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)