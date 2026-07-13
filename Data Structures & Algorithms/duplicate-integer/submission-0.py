class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()

        for n in nums:
            if n in unique_values:
                return True
            unique_values.add(n)

        return False
