class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        index = -1

        while left <= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
                mid = left + ((right - left) // 2)
            else:
                right = mid - 1
                mid = ((right - left) // 2)
            
            

        return index