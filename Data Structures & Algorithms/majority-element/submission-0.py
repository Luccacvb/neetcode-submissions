class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1

        max_v = 0
        res = 0
        for k, v in counter.items():
            max_v = max(max_v, v)
            if max_v == v:
                res = k

        return res
