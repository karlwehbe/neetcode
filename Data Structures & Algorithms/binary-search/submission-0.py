class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        index = -1

        while left <= right:
            print(left, mid, right)
            if nums[left] == target:
                index = left
                break
            elif nums[right] == target:
                index = right
                break
            elif nums[mid] == target:
                index = mid
                break

            if target > nums[mid]:
                left = mid + 1
                mid = left + ((right - left) // 2)
            else:
                right = mid - 1
                mid = ((right - left) // 2)
            
            

        return index