class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()

        for num in nums:
            if num not in numbers:
                numbers.add(num)
            else:
                return True
        
        return False