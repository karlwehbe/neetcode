class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # find rotation pivot (index of the minimum)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left

        # segment 1: nums[0:pivot], segment 2: nums[pivot:n]
        for seg_len, offset in ((pivot, 0), (n - pivot, pivot)):
            left, right = 0, seg_len - 1
            while left <= right:
                mid = left + (right - left) // 2
                val = nums[mid + offset]
                if val == target:
                    return mid + offset
                elif target > val:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1