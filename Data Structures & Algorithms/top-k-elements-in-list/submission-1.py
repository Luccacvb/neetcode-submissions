class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = count.most_common(k)
        res = []

        for t in top_k:
            res.append(t[0])

        return res
