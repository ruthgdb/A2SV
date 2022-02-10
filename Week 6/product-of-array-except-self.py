class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProduct = [1]
        product = 1
        res = []
        length = len(nums)
        
        for i in range(length-1,0,-1):
            product *= nums[i]
            prefProduct.append(product)
            
        product = 1  
        
        for i in range(length): 
            res.append(product * prefProduct.pop())
            product *= nums[i]
           
        return res