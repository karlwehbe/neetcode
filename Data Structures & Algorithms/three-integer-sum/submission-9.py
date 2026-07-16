class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Fix one number, then it's two sum: find a pair summing to -nums[i].
        # Sorted array lets two pointers solve that in one pass.
        nums.sort()
        sol = []

        for i in range(len(nums) - 2):
            # Anchor is the smallest of the triplet. 
            # Positive anchor means all three are positive, no zero sum possible.
            if nums[i] > 0:
                break

            # Same anchor value as last round finds the same triplets. Skip.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1   # everything right of l is bigger, grow the sum
                elif s > 0:
                    r -= 1   # everything left of r is smaller, shrink it
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # Equal values are adjacent after sorting, so skipping
                    # them here blocks all duplicate triplets.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return sol
