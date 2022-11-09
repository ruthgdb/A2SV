class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        first_num = 0
        second_num = 0

        for num in nums:
            xor ^= num

        i = 0

        while xor:
            if xor & (1 << i):
                break
            i += 1

        for num in nums:
            if num & (1 << i):
                first_num ^= num
            else:
                second_num ^= num

        return [first_num, second_num]