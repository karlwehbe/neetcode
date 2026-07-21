class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minimum = float("inf")
        
        while left <= right:
            mid = left + ((right - left) // 2)
            minimum = min(nums[mid], minimum)
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minimum