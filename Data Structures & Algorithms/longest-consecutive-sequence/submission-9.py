class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        nums = set(nums)
        curr_num = min(nums)
        max_num = max(nums)
        max_length = 0
        count = 1
        while curr_num < max_num:
            print(curr_num)
            if curr_num + 1 in nums:
                nums.remove(curr_num)
                count += 1
                curr_num += 1
            else:
                if count > max_length: max_length = count
                count = 1
                nums.remove(curr_num)
                curr_num = min(nums)
            

        if count > max_length: max_length = count
        return max_length