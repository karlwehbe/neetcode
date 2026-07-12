class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)

        pointers = []
        res = False

        for i in range(n):
            m = matrix[i]
            l, r = m[0], m[-1]
            pointers.append([l,r])        
        

        target_matrix = -1
        for i in range(n):
            m = matrix[i]
            l, r = pointers[i][0], pointers[i][1]

            if target >= l and target <= r:
                target_matrix = i
                
        if target_matrix == -1:
            return False


        left = 0
        right = len(matrix[target_matrix]) - 1
        mid = len(matrix[target_matrix]) // 2
        nums = matrix[target_matrix]

        while left <= right:
            if nums[mid] == target:
                return True

            if target > nums[mid]:
                left = mid + 1
                mid = left + ((right - left) // 2)
            else:
                right = mid - 1
                mid = ((right - left) // 2)
        
        return False

        

