class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        freq = [0] * 1001

        for n in nums:
            freq[n] += 1

        for n in range(1000, -1, -1):
            if freq[n] == 1:
                return n

        return -1
