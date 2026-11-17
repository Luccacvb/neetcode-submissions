class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        visited = set(nums)
        max_count = count = 1

        for v in visited:
            if (v - 1) not in visited:
                count = 1

                while (v + count) in visited:
                    count += 1

                max_count = max(max_count, count)

        return max_count
