class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                if nums[i] < 0:
                    return nums[i] * -1
                return nums[i]
            else:
                nums[abs(nums[i]) - 1] *= -1
            
        
        
        