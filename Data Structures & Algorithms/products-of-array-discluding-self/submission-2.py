class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        for i in range(1, len(l)):
            l[i] = l[i - 1] * nums[i - 1]

        r = [1] * len(nums)
        for i in range(len(r) - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        res = [1] * len(nums)
        for i in range(len(res)):
            res[i] = r[i] * l[i]

        return res
