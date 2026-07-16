class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        l, r = 0, len(nums) - 1
        for i in range(len(nums)):
            l, r = i, len(nums) - 1
            while l <= r:
                left_pointer = nums[l]
                right_pointer = nums[r]

                if left_pointer < 0:
                    target = -1 * (right_pointer + left_pointer)
                else:
                    target = -1 * (right_pointer - left_pointer)

                if target in nums[l+1: r]:
                    triplets = [left_pointer, right_pointer, target]
                    triplets.sort()
                    if triplets not in sol:
                        sol.append(triplets)
            
                r -= 1

        
        return sol



