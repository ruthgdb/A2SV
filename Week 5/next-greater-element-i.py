class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            for j in range(index, len(nums2)):
                temp = -2
                if j < len(nums2)-1 and nums2[index] < nums2[j+1]:
                    temp = nums2[j+1]
                    break
                else:
                    temp = -1
            res.append(temp)
        return res