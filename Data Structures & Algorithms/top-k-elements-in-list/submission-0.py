class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter()

        for n in nums:
            count[n] += 1

        res = []
        for i, v in count.most_common():
            if len(res) == k:
                return res
            res.append(i)

        return res
