class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        if nums[0] == 0 and len(nums) > 1:
            return False

        maxJump = 0
        for i in range(len(nums)-1):
            if maxJump < i:
                return False

            maxJump = max(i + nums[i], maxJump)


        if maxJump < len(nums)-1:
            return False

        return True