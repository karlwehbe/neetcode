class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = []
        product = 1
        for i in range(len(nums)):
            if i != 0:
                product = product * nums[i-1]
            prefix_product.append(product)
        
        print(prefix_product)
        
        suffix_product = [1 for i in range(len(nums))]
        product = 1
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if i != len(nums)-1:
                product = product * nums[i+1]
            suffix_product[i] = product
        
        solution = []
        for prefix, suffix in zip(prefix_product, suffix_product):
            solution.append(prefix * suffix)
        
        return solution