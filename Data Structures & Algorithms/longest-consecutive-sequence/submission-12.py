class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 1
        max_count = 1
        numbers = set(nums)

        for n in numbers:
            if (n - 1) not in numbers:
                while (n + count) in numbers:
                    count += 1
                max_count = max(max_count, count)

            count = 1

        return max_count
