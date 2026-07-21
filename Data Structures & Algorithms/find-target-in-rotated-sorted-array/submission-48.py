class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        minimum = float("inf")
        
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] < minimum:
                minimum = nums[mid]
                min_data = (minimum, mid)  
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(nums)-1
        maximum = float("-inf")
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] > maximum:
                maximum = nums[mid]
                max_data = (maximum, mid)  
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        

        arrays = []
        split = False
        if min_data[0] < max_data[0] and min_data[1] > max_data[1]:
            arrays.append(nums[:max_data[1]+1]) 
            arrays.append(nums[min_data[1]:])
            split = True
        else:
            arrays.append(nums)


        curr_arr = -1
        for array in arrays:
            curr_arr += 1
            left, right = 0, len(array)-1
           
            while left <= right:
                mid = left + ((right - left) // 2)
                if array[mid] == target:
                    if curr_arr == 1:
                        return mid + len(arrays[0])
                    return mid

                if target > array[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        