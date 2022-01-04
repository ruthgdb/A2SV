class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        for i in range(m,n+m):
            nums1[i] = nums2[index]
            index += 1
        nums1.sort()