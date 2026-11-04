class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i, v in enumerate(nums):
            res = target - v
            if res in mapp:
                return [mapp[res], i]

            mapp[v] = i

        return [-1, -1]
