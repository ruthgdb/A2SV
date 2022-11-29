import random

class RandomizedSet:

    def __init__(self):
        self.indices = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        idx = self.indices[val]
        self.indices[self.nums[-1]] = idx
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        del self.indices[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()