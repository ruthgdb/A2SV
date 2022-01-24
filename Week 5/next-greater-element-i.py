class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monoStack = [nums2[0]]
        greaterElement = {}
        
        for i in range(1, len(nums2)):
            while monoStack and (nums2[i] > monoStack[-1]):
                greaterElement[monoStack.pop()] = nums2[i]   
            monoStack.append(nums2[i])
            
        while monoStack:
            greaterElement[monoStack.pop()] = -1
       
        return [greaterElement[i] for i in nums1]