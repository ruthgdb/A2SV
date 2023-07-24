class SnapshotArray:

    def __init__(self, length: int):
        self.keys = [[(0, 0)] for _ in range(length)]
        self.indices = [[0] for _ in range(length)]
        self.snap_num = 0

    def set(self, index: int, val: int) -> None:
        if self.keys[index][-1][0] != self.snap_num:
            self.keys[index].append((self.snap_num, val))
            self.indices[index].append(self.snap_num)
        else:
            self.keys[index][-1] = (self.snap_num, val)

    def snap(self) -> int:
        self.snap_num += 1
        return self.snap_num - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.indices[index], snap_id)
        
        if i < len(self.keys[index]):
            if self.keys[index][i][0] != snap_id:
                i -= 1
                
            return self.keys[index][i][1]
        
        return self.keys[index][-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)