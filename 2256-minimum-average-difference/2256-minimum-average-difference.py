class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        first = [nums[0]]
        second = nums[1:]

        if len(nums) == 1:
            return 0

        v1 = sum(first)
        v2 = sum(second)
        l1 = 1
        l2 = len(nums) - 1

        currDiff = abs((v1 // l1) - (v2 // l2))
        currIndex = 0

        for i in range(1, len(nums)-1):
            if l1 == 0:
                v1 = 0
                l1 = 0
            else:
                v1 = (v1 + nums[i])
                l1 += 1


            if l2 == 0:
                v2 = 0
                l2 = 0
            else:
                v2 = (v2 - nums[i])
                l2 -= 1


            if currDiff > abs((v1 // l1) - (v2 // l2)):
                currDiff = abs((v1 // l1) - (v2 // l2))
                currIndex = i

        v1 = sum(nums[:]) // len(nums[:])

        if currDiff > abs(v1 - 0):
                currDiff = abs(v1 - 0)
                currIndex = len(nums)-1

        return currIndex