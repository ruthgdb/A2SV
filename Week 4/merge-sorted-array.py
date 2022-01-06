class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = 0
        for i in range(m,n+m):
            nums1[i] = nums2[x]
            x += 1
        nums1.sort()