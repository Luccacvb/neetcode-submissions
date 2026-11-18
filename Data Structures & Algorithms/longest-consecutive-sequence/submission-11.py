class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = max_count = 1
        uniq_nums = set(nums)

        for n in uniq_nums:
            if (n - 1) not in uniq_nums:
                while (n + count) in uniq_nums:
                    count += 1

                max_count = max(max_count, count)
            count = 1

        return max_count
