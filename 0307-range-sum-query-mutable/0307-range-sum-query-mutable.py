class NumArray:

    def __init__(self, nums: List[int]):
        # round up to the nearest power of 2
        self.length = 2 ** (math.ceil(math.log2(len(nums))))
        self.arr = [0] * (2 * self.length - 1)
        self.nums = nums
        
        # insert the numbers in the tree
        for i, num in enumerate(nums):
            self.arr[self.length - 1 + i] = num
            
        #bottom up
        for i in range(self.length - 2, -1, -1):
            self.arr[i] = self.arr[2 * i + 1] + self.arr[2 * i + 2]

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        start = self.length - 1 + index
        
        while start != 0:
            self.arr[start] += diff
            start = (start - 1) // 2
            
        self.arr[0] += diff
    
    def rangeSumFromZero(self, until):
        total = 0
        curr_ind = 0
        start = 0
        end = self.length - 1
        
        while curr_ind < self.length - 1:
            if (end + start) // 2 < until:
                total += self.arr[2 * curr_ind + 1]
                curr_ind = 2 * curr_ind + 2
                start = (end + start) // 2 + 1
            else:
                curr_ind = 2 * curr_ind + 1
                end = (end + start) // 2
                
        return total + self.arr[curr_ind]
                
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.rangeSumFromZero(right)
        
        return self.rangeSumFromZero(right) - self.rangeSumFromZero(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)