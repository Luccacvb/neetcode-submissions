class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordered = sorted(nums)
        res = []

        for i in range(len(ordered)):
            anchor = ordered[i]
            if anchor == ordered[i - 1] and i > 0 and i < len(ordered) - 1:
                continue

            l = i + 1
            r = len(ordered) - 1

            while l < r:
                total = ordered[l] + ordered[r] + anchor

                if total == 0:
                    if len(res) == 0 or [anchor, ordered[l], ordered[r]] != res[-1]:
                        res.append([anchor, ordered[l], ordered[r]])

                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res
